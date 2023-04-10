import requests
import xlwt
from lxml import etree
import csv

pages = range(1,201)
chart0 = str(input('请输入想要选择的频道（男频，女频）：'))
charts0 = {'男频':'0','女频':'3'}

chart1 = str(input('请输入想了解的排行榜（人气榜，新书榜，银票榜，互动榜，完本榜）: '))
charts1 = {'人气榜': 'hour72', '新书榜': 'potential', '银票榜': 'votes', '互动榜': 'interactive', '完本榜': 'wholebook'}

address_list = []

for page in pages:
    url = f'https://www.tadu.com/book/rank/list/{charts0[chart0]}-{charts1[chart1]}-0-0-{page}'
    resp = requests.get(url)
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.XML(resp.text, parser=parser)
    IDs = tree.xpath('/html/body/div[4]/article/div[2]/div')

    for ID in IDs:
        address = ID.xpath('./div[2]/div[1]/a/@href')[0]
        address_list.append([address])

ALLID = sum(address_list, [])
#print(address_list)

novel_list = []

for ad in ALLID:
    url = f'https://www.tadu.com{ad}'
    resp = requests.get(url)
    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.XML(resp.text, parser=parser)
    elements = tree.xpath('//*[@id="content"]/div[3]/div[1]/div')

    for element in elements:
        title = element.xpath('./div[2]/div[1]/a/text()')
        writer = element.xpath('./div[2]/div[1]/span/text()')
        words = element.xpath('./div[2]/div[3]/span[1]/em/text()')
        popularity = element.xpath('./div[2]/div[3]/span[2]/em/text()')
        sliverticket = element.xpath('./div[2]/div[3]/span[3]/em/text()')
        chapters = element.xpath('./div[3]/span[2]/i/text()')
        novel_list.append([title, writer, words, popularity, sliverticket, chapters])

for i in novel_list:
    print(i)

# 将数据存入csv文件
write = csv.writer(open('data.csv','w',encoding='utf-8'))
write.writerow(['title', 'writer', 'words', 'popularity', 'sliverticket', 'chapters'])
write.writerows(novel_list)

wb = xlwt.Workbook()
sheet = wb.add_sheet('data1')
titles = ('title', 'writer', 'words', 'weekpopularity', 'sliverticket', 'chapters')
for index, title in enumerate(titles):
    sheet.write(0, index, title)
for i, item in enumerate(novel_list):
    for j, val in enumerate(item):
        sheet.write(i + 1, j, val)
wb.save('data.xls')
