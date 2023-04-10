from urllib import request
import random
from lxml import etree
import pandas as pd
from threading import Thread


ua_list = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'User-Agent:Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
]
ua_list_number = len(ua_list)


def requestURL(url):
    headers = {
        'User-Agent': str(ua_list[random.randint(0, ua_list_number - 1)])}
    req = request.Request(
        url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    parse_html = etree.HTML(html)
    return parse_html


top_url = 'https://zh.weatherspark.com'


# header


def perLocation(lo, url):
    parse_html = requestURL(url)
    item = []
    dfs = parse_html.xpath('//*[@id="main"]/div[2]/div[3]/div/div/div/ul/li')
    for df in dfs:
        df_url = df.xpath('a/@href')
        location = df.xpath('a//text()')
        url = top_url + str(df_url[0])
        item += pageData(lo + '-' + location[0], url)

    name = ['地区', '1', '2', '3', '4', '5', '6', '7',
            '8', '9', '10', '11', '12']
    test = pd.DataFrame(columns=name, data=item)
    test.to_csv('E:\\31\\test3.csv', mode='a',
                encoding='gbk', index=None)

    return item


def pageData(lo, url):
    parse_html = requestURL(url)
    item = []
    # //*[@id="Report-Content"]/div[2]/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[3]
    cocpts = parse_html.xpath(
        '//*[@id="Report-Content"]/div[2]/div[2]/div[1]/table//tr/td/table//tr')
    # //*[@id = "Report-Content"]/div[2]/div[2]/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[1]/span

    for cptss in cocpts:
        tem = []
        cpts = cptss.xpath('td')
        for cpt in cpts:
            data = cpt.xpath('./text()')
            if '\n' != data[0]:
                tem.append(data[0])
        if (len(tem) != 0):
            item.append(tem)
    for i in item:
        i.insert(0, lo)

    return item


def EveryContry(url):

    global citys

    citys = input("输入特定城市: ")
    headers = {
        'User-Agent': str(ua_list[random.randint(0, ua_list_number - 1)])}
    req = request.Request(
        url=top_url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode()
    parse_html = etree.HTML(html)
    xpath_bds = '//*[@id="main"]/div[2]/div'
    r_list = parse_html.xpath(xpath_bds)
    for list in r_list:
        low_url = list.xpath('div/h3/a/@href')
        contry = list.xpath('div/h3/a//text()')
        if(low_url == []):
            return []
        url = top_url + str(low_url[0])
        for list in r_list:
            location = list.xpath('div/div/div/ul/li')
            for lo in location:
                location_url = lo.xpath('a/@href')
                city = lo.xpath('a//text()')
                if(citys == ''):
                    url = top_url + str(location_url[0])
                    perLocation(city[0], url)
                else:
                    if(citys == city[0]):
                        url = top_url + str(location_url[0])
                        perLocation(city[0], url)


EveryContry('https://zh.weatherspark.com')
