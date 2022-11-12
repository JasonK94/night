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
    while True:
        if (pa.locateOnScreen('sedu_donesign1.png', confidence=cf) or pa.locateOnScreen('sedu_donesign2.png', confidence=cf)):
            if pa.locateOnScreen('sedu_donesign1.png', confidence=cf):
                why=1
            elif pa.locateOnScreen('sedu_donesign2.png', confidence=cf):
                why=2
            else:
                why=0
            print(f'이 신호에 의해 다음으로 넘어갑니다. {why}')
            if pa.locateOnScreen('sedu_next.png', confidence=cf):
                xy=pa.position()
                pa.click(pa.center(pa.locateOnScreen('sedu_next.png', confidence=cf)))
                pa.moveTo(xy)
                print('code 1-1')
            else:
                print('버튼이 없어졌어요.')
                pa.sleep(10)
        elif pa.locateOnScreen('edu_start.png', confidence=cf):
            pa.click(pa.center(pa.locateOnScreen('edu_start.png', confidence=cf)))
            print('code 2-1')
        elif pa.locateOnScreen('edu_welldone.png',confidence=cf):
            pa.click(pa.center(pa.locateOnScreen('edu_end.png', confidence=cf)))
            print('code 2-2')
        elif pa.locateOnScreen('edu_lecture.png'):
            A=pa.locateOnScreen('edu_lecture.png')[1]
            for i, j in enumerate(pa.locateAllOnScreen('edu_lecturestart.png')):
                if j[1]>A:
                    B=j
                    break
                pass
            pa.click(pa.center(B))
            print('code 2-3')
        elif pa.locateOnScreen('edu_play.png'):
            pa.click(pa.center(pa.locateOnScreen('edu_play.png')))
            print('code 2-4')
        else:
            print(f'아직 재생 중입니다. {time.strftime("%H:%M:%S",time.localtime(time.time()))}')
        pa.sleep(30)