import pyautogui as pa
import keyboard as kb
import os
import time

from bs4 import BeautifulSoup as bs
from selenium import webdriver

os.chdir('D:/overnight')
path='C:/Users/user/OneDrive/util/chromedriver.exe'
url='https://www.youtube.com/watch?v=1_dpGP5wOO0'
cf=0.85

def turn_on_wr():
    driver=webdriver.Chrome(path)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.implicitly_wait(10)
    pa.click(pa.locateOnScreen('play_yt.png', confidence=cf))


while True and not kb.is_pressed('Esc'):
    if pa.locateOnScreen('phonecall.png', confidence=cf) or pa.locateOnScreen('phonedis.png', confidence=cf) or pa.locateOnScreen('phonecall2.png', confidence=cf):
        driver = webdriver.Chrome(path)
        driver.implicitly_wait(10)
        driver.get(url)
        driver.implicitly_wait(10)
        pa.click(pa.locateOnScreen('play_yt.png', confidence=cf))
        time.sleep(60)
    else:
        if int(time.strftime('%H', time.localtime(time.time())))<8:
            print(f'아직 별 일 없는 듯.... {time.strftime("%H:%M:%S",time.localtime(time.time()))}')
            XY=pa.locateOnScreen('phone_vertex.png')
            pa.moveTo(XY[0]+200, XY[1]+500)
            pa.scroll(-500)
            time.sleep(3)
            pa.scroll(500)
            time.sleep(10)
        else:
            print(f'퇴근하자')
            break