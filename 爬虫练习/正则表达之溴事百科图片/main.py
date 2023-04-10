import requests
import json
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url='https://www.huashi6.com/painter/7168'
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
        #'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    respsonse=requests.get(url=url,headers=header)
    respsonse.encoding = 'utf-8'
    page_text=respsonse.text
    filename='./鬼刀.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)
        print('保存成功！')
    soup=BeautifulSoup(page_text,'lxml')
    print(soup.select('.pc-body picture'))