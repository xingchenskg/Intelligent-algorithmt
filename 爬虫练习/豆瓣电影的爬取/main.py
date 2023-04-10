import requests
import json
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'
    #参数处理
    param={
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start': '0',
        'limit': '20'
    }
    #url伪装
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    respsonse=requests.get(url=url,params=param,headers=headers)
    list_data=respsonse.json()
    #持久化存储
    fp=open('./爬虫练习/豆瓣电影的爬取/douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over!')
