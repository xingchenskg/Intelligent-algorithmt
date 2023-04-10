import requests
from lxml import etree
from dama import YdmVerify


# 云打码识别验证码
def GetCodeText(code_img):
    Y = YdmVerify()
    with open(code_img, 'rb') as f:
        img_content = f.read()
    code_all_list = Y.common_verify(img_content)
    print('识别验证码结果为:',code_all_list)
    return code_all_list


if __name__ == '__main__':
    url='https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
    }
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    code_image_src='https://so.gushiwen.cn/'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    code_img='./code_img.jpg'
    img_data=requests.get(url=code_image_src,headers=headers).content
    with open(code_img,'wb') as fp:
        fp.write(img_data)
    code_text=GetCodeText(code_img)
