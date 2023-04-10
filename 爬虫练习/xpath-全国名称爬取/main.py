import requests
from lxml import etree
if __name__ == '__main__':
    url='https://www.aqistudy.cn/historydata/'
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=header).text
    tree=etree.HTML(page_text)
    # hot_li_list=tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names=[]
    # for li in hot_li_list:
    #     hot_city_name=li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    # all_li_list=tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in all_li_list:
    #     all_city_name=li.xpath('./a/text()')[0]
    #     all_city_names.append(all_city_name)
    all_city_names=[]
    a_list=tree.xpath('//div[@classs="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    for li in a_list:
        all_name=li.xpath('./a/text()')[0]
        all_city_names.append(all_name)
    print(all_city_names)
    
