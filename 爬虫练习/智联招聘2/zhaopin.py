from random import random
from time import sleep
import requests
from lxml import etree
import csv

# 更改爬取的页数
page_want = 3
# 更改爬取的城市范围
city_A = 530
city_B = 530

pages = range(1, page_want + 1)
cities = range(city_A, city_B + 1)
recruit_list = []
for city in cities:
    for page in pages:
        # 打印进度
        print('已完成', "{:.2f}".format(100 * ((city - city_A + 1) * page / ((city_B - city_A + 1) * page_want))),
              '%')
        sleep(int(random()))
        url = f'https://sou.zhaopin.com/?jl={city}&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&p={page}'
        headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',

            'Cookie': '21122523; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221159627791%22%2C%22first_id%22%3A%22186529c3ee5124e-087113506ac124-7a575473-1327104-186529c3ee6fd8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_utm_source%22%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22ty%22%2C%22%24latest_utm_content%22%3A%22tj2%22%2C%22%24latest_utm_term%22%3A%2200030815%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2NTI5YzNlZTUxMjRlLTA4NzExMzUwNmFjMTI0LTdhNTc1NDczLTEzMjcxMDQtMTg2NTI5YzNlZTZmZDgiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIxMTU5NjI3NzkxIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%221159627791%22%7D%2C%22%24device_id%22%3A%22186529c3ee5124e-087113506ac124-7a575473-1327104-186529c3ee6fd8%22%7D; at=03f8781f43a34dfeb8b9c0f193b7604f; rt=ab0b01d14a8943d8aa2d34b8766b4b76; acw_tc=ac11000116810948690952784e00dc86bc1b527f9af1847a87262fa54f519f; locationInfo_search={%22code%22:%22801%22%2C%22name%22:%22%E6%88%90%E9%83%BD%22%2C%22message%22:%22%E5%8C%B9%E9%85%8D%E5%88%B0%E5%B8%82%E7%BA%A7%E7%BC%96%E7%A0%81%22}; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1681094869; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1681095371'
        }
        resp = requests.get(url=url, headers=headers)
        parser = etree.HTMLParser(encoding='utf-8')
        tree = etree.XML(resp.text, parser=parser)
        paths = tree.xpath('//*[@id="positionList-hook"]/div/div')
        try:
            for path in paths:
                name_origin = path.xpath('./a/div[1]/div[1]/span/@title')
                # 有不包含数据的div标签，需要进行判断剔除，
                if not len(name_origin):
                    continue
                else:
                    name = name_origin[0].strip()
                company = path.xpath('./a/div[1]/div[2]/span/@title')[0].strip()
                salary = path.xpath('./a/div[2]/div[1]/p/text()')[0].strip()
                address = path.xpath('./a/div[2]/div[1]/ul/li[1]/text()')[0]
                experience = path.xpath('./a/div[2]/div[1]/ul/li[2]/text()')[0]
                academic_degree = path.xpath('./a/div[2]/div[1]/ul/li[3]/text()')[0]
                operating_model = path.xpath('./a/div[2]/div[2]/span/text()')[0]
                directions = path.xpath('./a/div[3]/div[1]/div/text()')
                direction_w = ''
                for direction in directions:
                    direction_w = direction + '|' + direction_w
                recruit_list.append(
                    [name, company, salary, address, experience, academic_degree, operating_model, direction_w])

        except:
            pass
f = open('recruit_data.csv', 'w', encoding='utf-8', newline='')
write = csv.writer(f)
write.writerow(
    ['name', 'company', 'salary', 'address', 'experience', 'academic_degree', 'operating_model', 'direction'])
write.writerows(recruit_list)
f.close()
