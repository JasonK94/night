import pyautogui as pa
import keyboard as kb
import os
import time
import pywinauto as pw

from bs4 import BeautifulSoup as bs
from selenium import webdriver

os.chdir('D:/overnight')
path='C:/Users/user/OneDrive/util/chromedriver.exe'

cf=0.95

while True and not kb.is_pressed('Esc'):
    while True:
        if (pa.locateOnScreen('edu_donesign.png', confidence=cf) or pa.locateOnScreen('edu_gauge_full.png', confidence=cf))\
                or (pa.locateOnScreen('edu_2_end.png', confidence=cf) or pa.locateOnScreen('edu_2_end2.png',confidence=cf))\
                or (pa.locateOnScreen('edu_donesign2.png', confidence=cf) or pa.locateOnScreen('edu_gauge_full2.png',confidence=cf)):
            if pa.locateOnScreen('edu_donesign.png', confidence=cf):
                print(pa.locateOnScreen('edu_donesign.png', confidence=cf))
                why=1
            elif pa.locateOnScreen('edu_gauge_full.png', confidence=cf):
                print(pa.locateOnScreen('edu_gauge_full.png', confidence=cf))
                why=2
            elif pa.locateOnScreen('edu_2_end.png', confidence=cf):
                why=3
            elif pa.locateOnScreen('edu_2_end2.png', confidence=cf):
                why=4
            elif pa.locateOnScreen('edu_donesign2.png', confidence=cf):
                why=5
            elif pa.locateOnScreen('edu_gauge_full2.png',confidence=cf):
                why=6
            else:
                why=0
            print(f'이 신호에 의해 다음으로 넘어갑니다. {why}')
            if why==0:
                pass
            else:
                if pa.locateOnScreen('edu_next.png', confidence=cf):
                    xy=pa.position()
                    pa.click(pa.center(pa.locateOnScreen('edu_next.png', confidence=cf)))
                    pa.moveTo(xy)
                    print('code 1-1')
                elif pa.locateOnScreen('edu_next2.png', confidence=cf):
                    xy = pa.position()
                    pa.click(pa.center(pa.locateOnScreen('edu_next2.png', confidence=cf)))
                    pa.moveTo(xy)
                    print('code 1-2')
                elif pa.locateOnScreen('edu_next3.png', confidence=cf):
                    xy = pa.position()
                    pa.click(pa.center(pa.locateOnScreen('edu_next3.png', confidence=cf)))
                    pa.moveTo(xy)
                    print('code 1-3')
                elif pa.locateOnScreen('edu_2_next.png', confidence=cf):
                    xy = pa.position()
                    pa.click(pa.center(pa.locateOnScreen('edu_2_next.png', confidence=cf)))
                    pa.moveTo(xy)
                    print('code 1-4')
                elif pa.locateOnScreen('edu_next4.png', confidence=cf):
                    xy = pa.position()
                    pa.click(pa.center(pa.locateOnScreen('edu_next4.png', confidence=cf)))
                    pa.moveTo(xy)
                    print('code 1-6')
                else:
                    print('버튼이 없어졌어요.')
                pa.sleep(10)
        elif pa.locateOnScreen('edu_start.png', confidence=cf):
            #시험문제 풀기
            pa.click(pa.center(pa.locateOnScreen('edu_start.png', confidence=cf)))
            print('code 2-1')
        elif pa.locateOnScreen('edu_welldone.png',confidence=cf):
            #강의 끝났을때
            pa.click(pa.center(pa.locateOnScreen('edu_end.png', confidence=cf)))
            print('code 2-2')
            pa.sleep(1)

        elif pa.locateOnScreen('edu_lecture.png'):
            #다음 강의 누르기
            A=pa.locateOnScreen('edu_lecture.png')[1]
            for i, j in enumerate(pa.locateAllOnScreen('edu_lecturestart.png')):
                if j[1]>A:
                    B=j
                    break
                pass
            pa.click(pa.center(B))
            print('code 2-3')
        elif pa.locateOnScreen('edu_play.png'):
            #첫 재생 버튼 누르기
            pa.click(pa.center(pa.locateOnScreen('edu_play.png')))
            print('code 2-4')
        else:
            print(f'아직 재생 중입니다. {time.strftime("%H:%M:%S",time.localtime(time.time()))}')
        pa.sleep(30)