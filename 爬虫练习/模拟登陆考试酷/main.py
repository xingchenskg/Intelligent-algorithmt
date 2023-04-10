import requests
from lxml import etree
from kuaidama import base64_api

#验证码识别
def GetCodeImg(img_path):
    result = base64_api(uname='xingchenskg', pwd='yc329750', img=img_path, typeid=3)
    print(result)
    return result

if __name__ == '__main__':
    url='https://examcoo.com/passport/login/preurl/L3VzZXJjZW50ZXI'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    code_img_src='https://examcoo.com'+tree.xpath('//*[@id="captchaImage"]/@src')[0]
    code_img_data=requests.get(url=code_img_src,headers=headers).content
    with open('./logcian.jpg','wb') as fp:
        fp.write(code_img_data)
    img_path = "E:\爬虫练习\模拟登陆考试酷\logcian.jpg"
    log_img_data=GetCodeImg(img_path)
    login_url='https://examcoo.com/passport/login/preurl/L3VzZXJjZW50ZXI'
    data={
        'uid': '10102016',
        'pwd': 'yc329750kaolaku',
        'pin': log_img_data,
        'timezone': 28800
    }
    response=requests.post(url=login_url,data=data,headers=headers)
    print(response.status_code)
    login_page_text=response.text
    with open('./kaoshiku.html','w',encoding='utf-8') as fp:
        fp.write(login_page_text)