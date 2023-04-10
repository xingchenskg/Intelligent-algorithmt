import re
import random
import requests
from lxml import etree
import xlwt
import time
import csv
if __name__ == '__main__':
    house_list = []
    # 多城市爬取
    citys = ['cd', 'bj', 'sh', 'sz', 'hz']
    for city in citys:
        # 多页爬取，这里爬取每个城市的1到10页的数据
        pages = range(1, 16)
        for page in pages:
            url = f'https://{city}.zu.anjuke.com/fangyuan/p{page}/'
            if city=='cd':
             city1='成都'
             print(f'=====正在从安居客上爬取成都市第{page}页租房数据====')
            if city=='bj':
             city1 = '北京'
             print(f'=====正在从安居客上爬取北京市第{page}页租房数据====')
            if city=='sh':
             city1 = '上海'
             print(f'=====正在从安居客上爬取上海市第{page}页租房数据====')
            if city=='sz':
             city1 = '深圳'
             print(f'=====正在从安居客上爬取深圳市第{page}页租房数据====')
            if city=='hz':
             city1 = '杭州'
             print(f'=====正在从安居客上爬取杭州市第{page}页租房数据====')
            headers = {
                'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
            }
            # 打开代理ip名的文件，因为这个网站在使用同一个ip进行多页爬取时会被识别为爬虫，然后被禁止访问，我们这里采用ip代理来伪装，就可以避免被识别出来
            f = open("IP.txt", "r")
            file = f.readlines()
            # 遍历并分别存入列表，方便随机选取IP
            item = []
            for proxies in file:
                proxies = eval(proxies.replace('\n', ''))  # 以换行符分割，转换为dict对象
                item.append(proxies)

            proxies = random.choice(item)  # 随机选取一个IP
            # 开始requests请求
            resp = requests.get(url, headers=headers, proxies=proxies)
            if resp.status_code==200:
                print('源码获取成功')
            paser = etree.HTMLParser(encoding="utf-8")
            tree = etree.XML(resp.text, paser)
            # 得到一页中所有房的数量
            houses = tree.xpath('//*[@id="list-content"]/div')
            length = len(houses)
            # 因为前面两个数据是页面数据，从三个开始才是房的数据，因此从第三个开始
            n = range(3, length)
            for i in n:
                title = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/h3/a/b/text()')[0].strip()
                price = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[2]/p/strong/b/text()')[0].strip()
                district = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/address/a/text()')[0].strip()
                address = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/address/text()')
                # 使用正则表达式去除空格，换行符问题
                a = ''.join(address)
                address1= re.sub(r'\s+', '', a)  # \s   匹配任意的空白符
                rentWay = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p/span[1][@class="cls-1"]/text()')[
                    0].strip()
                direction = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p/span[2][@class="cls-2"]/text()')[
                    0].strip()
                # elevator = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p/span[3][@class="cls-3"]/text()')[
                #     0].strip()
                subway = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p/span[4][@class="cls-4"]/text()')
                if subway == []:
                    subway = '未知'
                else:
                    subway = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p/span[4][@class="cls-4"]/text()')[ 0].strip()
                square = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p[1]/b[3]/text()')[0].strip()
                floor = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p[1]/text()[5]')[0].strip()
                # 由于这里的房户户型只能得到相应的数字，所以转换为字符串，进行相加即可
                a = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p[1]/b[1]/text()')[0].strip()
                b = tree.xpath(f'//*[@id="list-content"]/div[{i}]/div[1]/p[1]/b[2]/text()')[0].strip()
                houseType = a + '室' + b + '厅'
                house_list.append(
                    [title, price,city1,district, address1, rentWay, direction,  subway, square, floor, houseType])
            print('爬取成功')
            # 休眠两秒，防止爬取网页因为访问太快而识别出你是爬虫
            time.sleep(2)

# 将文件写入excel文件中
# wb = xlwt.Workbook()
# sheet = wb.add_sheet('data5')
# titles = (
#     'title', ' price','city',' district', 'address', 'rentWay', 'direction',  'subway', 'square', 'floor','houseType'
#  )
# # enumrate将数据系列中每一个参数分为索引和内容两部
# for index, title in enumerate(titles):
#     sheet.write(0, index, title)
# for i, item in enumerate(house_list):
#     for j, element in enumerate(item):
#         sheet.write(i + 1, j, element)
# wb.save('data_house1.xls')
header= (
    'title', ' price','city',' district', 'address', 'rentWay', 'direction',  'subway', 'square', 'floor','houseType'
 )
with open('c.csv', 'w', encoding='utf-8', newline='') as f:  # newline=''为写入时不添加的空行

     write = csv.writer(f)
    # 2.写入表头
     write.writerow(header)
        # writerow(序列) 写入单行
     write.writerows(house_list)
        # 3.写入内容



# print(title)
    # print(price)
    # print(district)
    # print(address)
    # print(rentWay)
    # print(direction)
    # print(elevator)
    # print(subway)
    # print(square)
    # print(floor)
    # print(houseType)
