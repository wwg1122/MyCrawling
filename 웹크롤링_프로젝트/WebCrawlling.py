import site
from platform import java_ver

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

def find_CoffeeBean_store(site) -> None:
    URLs = 'https://www.coffeebeankorea.com/store/store.asp'
    wd = webdriver.Chrome() #크롬 브라우저
    time.sleep(2) #페이지 연결 2초 기다림.
    for i in range(1,10): # 매점 갯수
        wd.get(URLs)
        time.sleep(1)
        try:
            wd.execute_script(f"storePop2({i})")
            time.sleep(1)
            html = wd.page_source
            soup = BeautifulSoup(html, "html.parser")
            name = soup.select("div.store_txt")
            print(name)
            pass
        except Exception as ex:
            print("웹브라우저 오류")
            pass

find_CoffeeBean_store("커피빈")