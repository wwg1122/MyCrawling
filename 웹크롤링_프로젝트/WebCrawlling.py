import site
from platform import java_ver

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

def find_CoffeeBean_store(information) -> None:
    URLs = 'https://www.coffeebeankorea.com/store/store.asp'
    wd = webdriver.Chrome() #크롬 브라우저
    time.sleep(1) #페이지 연결 2초 기다림.



    for i in range(1,410): # 매점 갯수
        wd.get(URLs)
        time.sleep(2)
        try:
            wd.execute_script(f"storePop2({i})")
            time.sleep(1)
            html = wd.page_source
            soup = BeautifulSoup(html, "html.parser")
            name = soup.select("div.store_txt > h2")
            print(name[0].text)
            address = soup.select('div.store_txt > table.store_table > tbody > tr > td')
            print(address[2].text)
            information.append(name[0].text + ',' + address[2].text)
            pass
        except Exception as ex:
            print("웹브라우저 오류")
            pass

coffee_bean_data = []
find_CoffeeBean_store(coffee_bean_data)
pandas_form = pd.DataFrame(coffee_bean_data, columns = ('store_name', 'address'))
pandas_form.to_csv('CoffeeBean_EXCEL.csv', index=False, encoding='cp949')
pandas_form.to_csv('CoffeeBean_EXCEL.csv', index=False, encoding='utf-8')