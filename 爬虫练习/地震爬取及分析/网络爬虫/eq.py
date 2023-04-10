# coding=utf-8
import xlwt
from time import sleep
import requests
import json
import csv

if __name__ == '__main__':
    url = 'http://www.ceic.ac.cn/ajax/search'
    headers = {
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=297b5faa7b4f001aa5c359ed2b4bbd49',
        'DNT': '1',
        'Referer': 'http://www.ceic.ac.cn/history',
        'Host': 'www.ceic.ac.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data_list = [] # 初始化Exsel临时数据列表
    titles = ['AUTO_FLAG', 'CATA_ID', 'CATA_TYPE', 'EPI_DEPTH', 'EPI_LAT',
             'EPI_LON', 'EQ_CATA_TYPE', 'EQ_TYPE', 'IS_DEL', 'LOCATION_C',
             'LOCATION_S', 'LOC_STN', 'M', 'M_MB', 'M_MB2',
             'M_ML', 'M_MS', 'M_MS7', 'NEW_DID', 'O_TIME',
             'O_TIME_FRA', 'SAVE_TIME', 'SUM_STN', 'SYNC_TIME', 'id']
    # 断点记录文件
    seq_f = open('seq', 'a+', encoding='utf-8', newline='')
    while True:
        i_times = input("是否第一次爬取(y/n)")
        if i_times == 'y':
            start = int(input("开始页数[>=1]:"))
            end = int(input("结束页数[<=554]:"))
            seq_s = start
            if start < 1 or end > 554 or start > end:
                print('超出可爬取页数或设置非法')
                continue
            else:
                f = open('recruit_data.csv', 'w', encoding='utf-8', newline='')
                break
        else:
            end = int(input("结束页数[<=554]:"))
            seq_f.seek(0)
            seq_s = int(seq_f.readline())
            seq_f.truncate()  # 清空断点记录文件中的数据
            if end >554:
                print('超出可爬取页数或设置非法')
                continue
            else:
                f = open('recruit_data.csv', 'a', encoding='utf-8', newline='')
                break
    write = csv.writer(f)
    write.writerow(titles)
    try:
        for i in range(seq_s, end+1):
            sleep(1)
            data = {'page':i,
                    'start': '2000-02-22',
                    'end': '2023-02-23',
                    'jingdu1':'',
                    'jingdu2':'',
                    'weidu1':'',
                    'weidu2':'',
                    'height1':'',
                    'height2':'',
                    'zhenji1':'',
                    'zhenji2':'',
                    'callback': 'jQuery18009668320735656395_1677155814904',
                    '_': '1677155828632'}
            eq_datas = requests.get(url, params=data,headers=headers)
            eq_list=[]
            if eq_datas.status_code == requests.codes.ok:
                data_json=eq_datas.text[41:-1]
                data_dict = json.loads(data_json)
                for element in data_dict['shuju']:
                    eq_list.append(
                        [element['AUTO_FLAG'], element['CATA_ID'], element['CATA_TYPE'],
                         element['EPI_DEPTH'], element['EPI_LAT'], element['EPI_LON'],
                         element['EQ_CATA_TYPE'], element['EQ_TYPE'], element['IS_DEL'],
                         element['LOCATION_C'], element['LOCATION_S'], element['LOC_STN'],
                         element['M'], element['M_MB'], element['M_MB2'],
                         element['M_ML'], element['M_MS'], element['M_MS7'],
                         element['NEW_DID'], element['O_TIME'], element['O_TIME_FRA'],
                         element['SAVE_TIME'], element['SUM_STN'], element['SYNC_TIME'],
                         element['id']])
                    # 保存到Excel中的列表
                    data_list.append(
                        [element['AUTO_FLAG'], element['CATA_ID'], element['CATA_TYPE'],
                         element['EPI_DEPTH'], element['EPI_LAT'], element['EPI_LON'],
                         element['EQ_CATA_TYPE'], element['EQ_TYPE'], element['IS_DEL'],
                         element['LOCATION_C'], element['LOCATION_S'], element['LOC_STN'],
                         element['M'], element['M_MB'], element['M_MB2'],
                         element['M_ML'], element['M_MS'], element['M_MS7'],
                         element['NEW_DID'], element['O_TIME'], element['O_TIME_FRA'],
                         element['SAVE_TIME'], element['SUM_STN'], element['SYNC_TIME'],
                         element['id']])
                # 计算当前的进度
                print(str((i-seq_s+1) / (end-seq_s +1)* 100) + '%')
                write.writerows(eq_list)
                seq_f.seek(0)
                seq_f.truncate()  # 清空断点记录文件中的数据
                seq_f.write(str(i))
            else:
                print(eq_datas)
    except:
        f.close()
        seq_f.close()
        exit(0)
    # 创建工作簿
    wb = xlwt.Workbook()
    # # 创建工作表
    sheet = wb.add_sheet('eq_data')
    # enumerate方法将接收数据系列，并将数据系列中的每一个参数分解为两个部分数据，
    #       第一个部分为本数据所在数据系列中的索引位置，第二部分为数据本身
    for index, data in enumerate(titles):
        sheet.write(0, index, data)
    for i, item in enumerate(data_list):
        for j, val in enumerate(item):
            sheet.write(i + 1, j, val)
    wb.save('eq_data.xls')
    print("DOWN")
    seq_f.truncate()
    seq_f.write('1')
    f.close()
    seq_f.close()