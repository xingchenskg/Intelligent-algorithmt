# utf8

import numpy as np
import pandas as pd
import scipy


class AutoBins:

    """
    20190331：更新，修改了 f-string 以适应 python 3.5 版本
    """

    def __init__(self, frame, y):
        self._frame = frame.copy()
        self._y = y

    def _column_qcut(self, column):

        # 进行初始化分箱，先分成 20 个箱体
        _, bins = pd.qcut(self._frame[column], q=20, retbins=True, duplicates="drop")

        # 排除因为开闭区间导致的临界值取值问题
        bins = list(bins)
        bins.insert(0, -float("inf"))
        bins[-1]= float("inf")

        # 按照添加了最大最小值后的箱体重新分箱
        self._frame[column+"_qcut"] = pd.cut(self._frame[column], bins=bins)

        init_counts = list(self._frame[column+"_qcut"].value_counts(sort=False))
        # 查看首尾箱体是否占比超过 2%，如果没有那么将之与相邻的箱体进行合并，用于处理添加 inf 后导致的空字段的问题
        if init_counts[0] < (len(self._frame)/50):
            bins.pop(1)
        if init_counts[-1] < (len(self._frame)/50):
            bins.pop(-2)

        # 使用这个箱体的数据进行分箱并做后续的最优化合并
        self._frame[column+"_qcut"] = pd.cut(self._frame[column], bins=bins)
        # 统计每个分段 0，1的数量
        inf_init_bins = self._frame.groupby([column+"_qcut", self._y])[self._y].count().unstack(fill_value=0)
        # num_bins值分别为每个区间的上界，下界，0的频次，1的频次
        num_bins = [*zip(bins, bins[1:], inf_init_bins[0], inf_init_bins[1])] # 0，1 表示 Y 的取值
        return num_bins

    def _merge_zero_bins(self, num_bins):
        # 用于确保所有的分组均包含两种分类
        idx = 0
        while idx < len(num_bins):
            # 如果是第一个组某个分类为 0，向后合并
            if 0 in num_bins[0][2:]:
                num_bins = self._merger_bins(num_bins, idx)
                continue
            else:
                # 如果后面的组某个分类为 0 ，向前合并，合并后 num_bins 变短
                # 所以需要继续查看当前的 idx 的位置
                if 0 in num_bins[idx][2:]:
                    num_bins = self._merger_bins(num_bins, idx-1)
                    continue
                else:
                    # 如果没有出现某个分类统计为 0 ，查看下一个 idx 的位置
                    idx += 1
        return num_bins

    def _merger_bins(self, num_bins, x):
        # 合并 num_bins x 索引和 x+1 索引的分组数据
        num_bins[x: x+2] = [(
            num_bins[x][0],
            num_bins[x+1][1],
            num_bins[x][2]+num_bins[x+1][2],
            num_bins[x][3]+num_bins[x+1][3]
        )]
        return num_bins

    # 创建计算 iv 值函数
    def _get_iv(self, woe_df):
        rate = ((woe_df.count_0/woe_df.count_0.sum()) -
                (woe_df.count_1/woe_df.count_1.sum()))
        iv = np.sum(rate * woe_df.woe)
        return iv


    # 定义计算 woe 的函数
    def _get_woe(self, num_bins):
        # 通过 num_bins 数据计算 woe
        columns = ["min", "max", "count_0", "count_1"]
        df = pd.DataFrame(num_bins, columns=columns)

        df["total"] = df.count_0 + df.count_1
        df["percentage"] = df.total / df.total.sum()
        df["bad_rate"] = df.count_1 / df.total
        df["woe"] = np.log(
            (df.count_0 / df.count_0.sum()) /
            (df.count_1 / df.count_1.sum())
            )
        return df

    def _chi2_merge(self, num_bins):
        p_values = []
        # 获取 num_bins 两两之间的卡方检验的置信度（或卡方值）
        for i in range(len(num_bins)-1):
            x1 = num_bins[i][2:]
            x2 = num_bins[i+1][2:]
            # 0 返回 chi2 值，1 返回 p 值。
            pv = scipy.stats.chi2_contingency([x1, x2])[1]
            # chi2 = scipy.stats.chi2_contingency([x1, x2])[0]
            p_values.append(pv)

        # 通过 p 值进行处理。合并 p 值最大的两组
        idx = p_values.index(max(p_values))
        num_bins = self._merger_bins(num_bins, idx)
        return num_bins

    def auto_bins(self, column, n=2, show_iv=True):
        print("对 {} 列进行分箱: ".format(column))
        # 初始化分箱
        num_bins = self._column_qcut(column)
        # 合并没有包含两类的分箱
        num_bins = self._merge_zero_bins(num_bins)
        # 通过 chi2_merge 不断合并最相似的相邻箱体
        while len(num_bins) > n:
            num_bins = self._chi2_merge(num_bins)
            woe_df = self._get_woe(num_bins)
            iv = self._get_iv(woe_df)
            if show_iv:
                print("分组个数: {:02d} \tiv值: {}".format(len(num_bins),iv))

        woe_df = self._get_woe(num_bins)
        iv = self._get_iv(woe_df)
        if show_iv:
            print("\n最后分箱情况: ")
            print("分组个数: {:02d} \tiv值: {}".format(len(num_bins),iv))
            print("\n分组woe情况：")
            print(woe_df)
        return num_bins, woe_df, iv

