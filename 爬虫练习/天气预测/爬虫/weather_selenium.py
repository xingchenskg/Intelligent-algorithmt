import time
import pic as pic
from selenium import webdriver
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
url='https://weather.cma.cn/web/text/HB/ABJ.html'
web = webdriver.Chrome('E:\download\chromedriver_win32\chromedriver.exe')
web.get(url)
web.maximize_window()
# web.execute_script(('window.scrollTo(0,475)'))
regions = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/ul')[0].text
weather_list = []
city_name_list=[]
morn_weather_list=[]
morn_wind_d_list =[]
morn_wind_l_list =[]
morn_Htemp_list =[]
night_weather_list =[]
night_wind_d_list =[]
night_wind_l_list =[]
night_Ltemp_list =[]
# urls = web.find_elements(By.XPATH,'/html/body/div[1]/div/div/div/div/div/div/a')[0].get_attribute('href')
# for region in  regions:
    ##定位地区并选择
for i in range(1,9):
    region = web.find_element(By.XPATH,f'/html/body/div[1]/div[3]/div/div/ul/li[{i}]/a')
    region.click()
    cities = web.find_elements(By.XPATH, f'/html/body/div[1]/div[3]/div/div/div/div[{i}]/div')[0].text
    #定位城市并选择
    for j in range(1,len(cities.split(' '))+1):
        city = web.find_element(By.XPATH,f'/html/body/div[1]/div[3]/div/div/div/div[{i}]/div/a[{j}]')#/html/body/div[1]/div[3]/div/div/div/div[2]/div/a[1]
        city.click()
        dates = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/ul')[0].text
        #定位日期并选择
        for x in range(1,8):
            date = web.find_element(By.XPATH,f'/html/body/div[1]/div[3]/div/div/div/div[9]/ul/li[{x}]/a')
            date.click()
            city_name = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[1]')
            morn_weather = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[2]')
            morn_wind_d = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[3]')
            morn_wind_l = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[4]')
            morn_Htemp = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[5]')
            night_weather = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[6]')
            night_wind_d = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[7]')
            night_wind_l = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[8]')
            night_Ltemp = web.find_elements(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div[9]/div/div[1]/table/tbody/tr/td[9]')
            for z in city_name:
                city_name_list.append(z.text.strip())
            for a in morn_weather:
                morn_weather_list.append(a.text.strip())
            for s in  morn_wind_d:
                 morn_wind_d_list.append(s.text.strip())
            for d in morn_wind_l:
                 morn_wind_l_list.append(d.text.strip())
            for f in morn_Htemp:
                 morn_Htemp_list.append(f.text.strip())
            for g in night_weather:
                 night_weather_list.append(g.text.strip())
            for h in night_wind_d:
                 night_wind_d_list.append(h.text.strip())
            for j in night_wind_l:
                 night_wind_l_list.append(j.text.strip())
            for k in night_Ltemp:
                 night_Ltemp_list.append(k.text.strip())
weather_list.append([city_name_list,morn_weather_list,morn_wind_d_list,morn_wind_l_list,morn_Htemp_list,night_weather_list,night_wind_d_list,night_wind_l_list,night_Ltemp_list])
print(weather_list)




# for region in regions:
#
# print(regions)
# print(cities)
# print(dates)

# #自动下拉
# max_y = 10000
# y = 0
# while y<max_y:
#     web.execute_script(f'window.scrollTo(0,{y})')
#     y+=1000
#     time.sleep(1)

# title = web.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[1]/div/div[4]/a/em').text
# pic = web.find_element(By.XPATH, '//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').get_attribute('scr')
# price = web.find_element(By.XPATH,'//*[@id="J_goodsList"]/ul/li[1]/div/div[3]/strong/i').text
# next = web.find_element(By.XPATH,'//*[@id="J_bottomPage"]/span[1]/a[9]')
# next.click()

