
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from selenium.webdriver.chrome.service import Service

# 创建浏览器对象
path_driver=Service("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
web=webdriver.Chrome(service=path_driver)


# 进行请求
url = 'https://music.163.com/artist?id=5771'
web.get(url)
web_page = web.page_source

# 进入iframe标签
web.switch_to.frame(web.find_element(By.XPATH, '//*[@id="g_iframe"]'))
elements_list = web.find_elements(By.XPATH, '//div/div/div/div[1]/table/tbody/tr')
music_id_list = []
# music_id = web.find_element(By.XPATH, '//div/div/div/div[1]/table/tbody/tr[1]/td[1]/div/span[1]').get_attribute('data-res-id')
# print(music_id)
for element in elements_list:
    music_id = element.find_element(By.XPATH, './td[1]/div/span[1]').get_attribute('data-res-id')
    music_name = element.find_element(By.XPATH, './td[2]/div/div/div/span/a/b').get_attribute('title')
    music_url = f'https://music.163.com/song/media/outer/url?id={music_id}.mp3'
    music_resp = requests.get(music_url)
    music_con = music_resp.content

#要创建一个空的music文件
    music_f = open(f'music\\music{music_name}.mp3', 'wb')
    music_f.write(music_con)
    print(f'{music_name},已下载')

# /html/body/div[3]/div[1]/div/div/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[3]/td[1]/div/span[1]
# /html/body/div[3]/div[1]/div/div/div[3]/div[2]/div/div/div/div[1]/table/tbody/tr[2]/td[1]/div/span[1]