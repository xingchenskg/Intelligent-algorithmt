import requests
from lxml import etree
import re
if __name__ == '__main__':
    url='https://www.pearvideo.com/category_5'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    data_page=requests.get(url=url,headers=headers)
    data_page.encoding='utf-8'
    page_text=data_page.text
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//ul[@id="listvideoListUl"]/li')
    url_list=[]
    for li in li_list:
        detail_url='https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
        url_name=li.xpath('./div/a/div[2]/text()')[0]
        print(detail_url,url_name)
        detail_page_text=requests.get(url=detail_url,headers=headers).text
        filename='./'+url_name+'.html'
        # with open(filename,'w',encoding='utf-8') as fp:
        #     fp.write(detail_page_text)
        #     print(filename,'保存成功！')
        detail_tree=etree.HTML(detail_page_text)
        video_url=detail_tree.xpath('//div[@id="JprismPlayer"]/video/@src')

        # https: // www.pearvideo.com / videoStatus.jsp?contId = 1764042 & mrd = 0.6706870270351315
        # https: // www.pearvideo.com / videoStatus.jsp?contId = 1749821 & mrd = 0.43927990466379185
        0.8274255383635709