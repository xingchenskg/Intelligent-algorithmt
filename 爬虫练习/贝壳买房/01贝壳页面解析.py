import requests
from lxml import etree
import csv
import xlwt
# 输入城市的中文名，程序将指定城市进行爬取
# from xpinyin import Pinyin
Dict = {
    '成都': 'cd', '北京': 'bj', '西安': 'xa', '上海': 'sh', '苏州': 'sz'
}
cities = input('请输入城市名：')

pages = range(1, 7)
house_list = []
# cities = ['bj','sh','cd','xa','sz']
# for city in cities:
for page in pages:
    url = f'https://{Dict[cities]}.zu.ke.com/zufang/pg{pages}/#contentList'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Cookie':'lianjia_uuid=3d928fb9-0c20-4176-87df-44ce04d95135; lianjia_ssid=e22d9901-767d-4573-ba21-d4a5878757b3; select_city=510100; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiN2FjZDNkYTQ0YTdhY2U3MGRjMGRkODk0OThjODNkZWFhN2RmNWMxMzUyYmNiMDIyYWQ0NjA4NjI3YmNkODE4OGJmZWM3MmIzOWE3OWZiNDc4M2Y2OTk4NWMwZGJkMDNhMDExMGI4OTA3ZDFhNTUwNjM1NGUyYWJlOWUzZjY3ZDMyOGY1YzI3ZGFiNjRlOWNlNzE3MmQyYzI2YmQxNjlhZGJmNWI3NjI3NmE3NWMyOWM2YzdhYjdjZjA3NzAxNTA3OGJkMzBjNWM4OGMzYTFiYmQ0NThjNzc5ZTUxNTZjYjY2OTM5NTQxMjg0MTExNDI4ZGRjMjU0OTdhOWM2N2NlMlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhMmI4ZmM3Y1wifSIsInIiOiJodHRwczovL2NkLnp1LmtlLmNvbS96dWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='}
    resp = requests.get(url, headers=headers)

    # 确定编码
    parser = etree.HTMLParser(encoding='utf-8')

    # 建立tree对象
    tree = etree.XML(resp.text, parser=parser)

    elements_list = tree.xpath('//*[@id="content"]/div[1]/div[1]/div')
    try:
        for elements in elements_list:
            title = elements.xpath('./div/p[1]/a/text()')[0].strip()
            price = elements.xpath('./div/span/em/text()')[0].strip()
            ear = elements.xpath('./div/p[2]/a[1]/text()')[0]
            location = elements.xpath('./div/p[2]/a[2]/text()')[0]
            position = elements.xpath('./div/p[2]/a[3]/text()')[0]

            erea1 = elements.xpath('./div/p[2]/text()[last()-3]')[0].strip()
            erea2 = elements.xpath('./div/p[2]/text()[last()-2]')[0].strip()
            erea3 = elements.xpath('./div/p[2]/text()[last()-1]')[0].strip()
            house_list.append([title, price, ear, location, position, erea1, erea2, erea3])
    except:
        pass

# 将数据存入csv文件
# write = csv.writer(open('house_data.csv','w',encoding='utf_8'))
# write.writerow(['title', 'price', 'ear', 'location', 'position', 'erea1', 'erea2', 'erea3'])
# write.writerows(house_list)
# for i in house_list:
#     print(i)


# day04
# 将数据存入excel文件

# 创建工作簿
wb = xlwt.Workbook()
# # 创建工行表
sheet = wb.add_sheet('data1')
# # 在表格第一行写入列名
# enumerate方法将接收数据系列，并将数据系列中的每一个参数分解为两个部分数据，
#       第一个部分为本数据所在数据系列中的索引位置，第二部分为数据本身
titles = ('title', 'price', 'ear', 'location', 'position', 'erea1', 'erea2', 'erea3')
for index, data in enumerate(titles):
    sheet.write(0, index, data)

for i, item in enumerate(house_list):
    for j, val in enumerate(item):
        sheet.write(i+1, j, val)

wb.save('data_house.xls')

