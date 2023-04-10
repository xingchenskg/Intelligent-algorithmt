import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url='https://www.shicimingju.com/book/hongloumeng.html'
    header={
        'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    respsonse=requests.get(url=url,headers=header)
    respsonse.encoding='utf-8'
    page_text=respsonse.text
    soup=BeautifulSoup(page_text,'lxml')
    li_list=soup.select('.book-mulu>ul>li')
    fp=open('./红楼梦.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.a.string
        detail_url='https://www.shicimingju.com'+li.a['href']
        detail_respsonse=requests.get(detail_url,headers=header)
        detail_respsonse.encoding='utf-8'
        detail_text=detail_respsonse.text
        detail_soup=BeautifulSoup(detail_text,'lxml')
        de_tag=detail_soup.find('div',class_='chapter_content')
        content=de_tag.get_text()
        fp.write(title+':'+content+'\n')
        print(title,'保存成功！')