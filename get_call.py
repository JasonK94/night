import pyautogui as pa
import keyboard as kb
import os
import time

from bs4 import BeautifulSoup as bs
from selenium import webdriver

from twilio.rest import Client

os.chdir('D:/overnight')
path='C:/Users/user/OneDrive/util/chromedriver.exe'
url='https://www.youtube.com/watch?v=1_dpGP5wOO0'
cf=0.85

sid='ACfcc99664b89dbc225561f7000a836305'
token='c6f57cc082fc9c5b58822f99496a6926'
client=Client(sid, token)
"""
def turn_on_wr():
    driver=webdriver.Chrome(path)
    driver.implicitly_wait(10)
    driver.get(url)
    driver.implicitly_wait(10)
    pa.click(pa.locateOnScreen('play_yt.png', confidence=cf))

    message = client.messages \
        .create(body='전화왔어요', from_='+19204770393', to='+821083782358')
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to='+821083782358',
        from_='+19204770393'
    )
"""
while True and not kb.is_pressed('Esc'):
    pw.application.Application().connect(handle=133152).top_window().set_focus()
    if pa.locateOnScreen('phonecall.png', confidence=cf) or pa.locateOnScreen('phonedis.png', confidence=cf) or pa.locateOnScreen('phonecall2.png', confidence=cf):
        driver = webdriver.Chrome(path)
        driver.implicitly_wait(10)
        driver.get(url)
        driver.implicitly_wait(10)
        pa.click(pa.locateOnScreen('play_yt.png', confidence=cf))
        message = client.messages \
            .create(body='전화왔어요', from_='+19204770393', to='+821083782358')
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to='+821083782358',
            from_='+19204770393'
        )
        time.sleep(60)


    else:
        if int(time.strftime('%H', time.localtime(time.time())))<24:
            print(f'아직 별 일 없는 듯.... {time.strftime("%H:%M:%S",time.localtime(time.time()))}')
            xy = pa.position()
            XY=pa.locateOnScreen('phone_vertex.png')
            pa.moveTo(XY[0]+200, XY[1]+500)
            pa.scroll(-500)
            time.sleep(3)
            pa.scroll(500)
            pa.moveTo(xy)
            time.sleep(298)
        else:
            print(f'퇴근하자')
            break