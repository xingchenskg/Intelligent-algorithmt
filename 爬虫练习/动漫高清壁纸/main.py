import requests
from lxml import etree
import os
if __name__ == '__main__':
    path='./彼岸高清壁纸/'
    if not os.path.exists(path):
        os.mkdir(path)
    url='https://pic.netbian.com/new/index_{}.html'
    data={

    }
    header={

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    for i in range(30,35):
        respsonse=requests.get(url=url.format(i+1),headers=header)
        respsonse.encoding='gbk'
        page_text=respsonse.text
        tree=etree.HTML(page_text)
        li_list=tree.xpath('//div[@class="slist"]/ul/li')
        for li in li_list:
            img_src=li.xpath('./a/img/@src')[0]
            detail_url='https://pic.netbian.com'+img_src
            img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
            de_respsonse=requests.get(url=detail_url,headers=header).content
            with open(path+img_name,'wb') as fp:
                fp.write(de_respsonse)
                print(img_name,'下载成功！')