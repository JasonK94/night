import pyautogui as pa
import keyboard as kb
import os
import time
import pywinauto as pw

from bs4 import BeautifulSoup as bs
from selenium import webdriver

os.chdir('D:/overnight')
path='C:/Users/user/OneDrive/util/chromedriver.exe'

cf=0.85

while True and not kb.is_pressed('Esc'):
    if pa.locateOnScreen('edu_donesign.png', confidence=cf):
        if pa.locateOnScreen('edu_next.png', confidence=cf):
            xy=pa.position()
            pa.click(pa.center(pa.locateOnScreen('edu_next.png', confidence=cf)))
            pa.moveTo(xy)
        elif pa.locateOnScreen('edu_next2.png', confidence=cf):
            xy = pa.position()
            pa.click(pa.center(pa.locateOnScreen('edu_next2.png', confidence=cf)))
            pa.moveTo(xy)
        elif pa.locateOnScreen('edu_next3.png', confidence=cf):
            xy = pa.position()
            pa.click(pa.center(pa.locateOnScreen('edu_next3.png', confidence=cf)))
            pa.moveTo(xy)
        else:
            print('버튼이 없어졌어요.')
    else:
        print(f'아직 재생 중입니다. {time.strftime("%H:%M:%S",time.localtime(time.time()))}')
        pa.sleep(30)