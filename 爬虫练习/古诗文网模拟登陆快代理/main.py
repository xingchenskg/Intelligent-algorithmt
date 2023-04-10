import requests
from lxml import etree
from kuaidama import base64_api

if __name__ == '__main__':
    url="https://gushiwen.com/main/login.html"
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=header).text
    tree=etree.HTML(page_text)
    img_url=tree.xpath('//div[@id="main"]/div/div/form/div/ul/li[3]/img/@src')[0]
    img_text_url='https://gushiwen.com'+img_url
    img_data=requests.get(url=img_text_url,headers=header).content
    with open('./logician.jpg','wb') as fp:
        fp.write(img_data)
    img_path ="E:/爬虫练习/模拟登陆古诗文网站/logician.jpg"
    result = base64_api(uname='账户',pwd='密码',img=img_path,typeid=1001)
    print(result)
    # id=result['data']['id']
    # result = reportError(id)
    # print(result)
