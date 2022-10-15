########토큰을 업데이트하세요#########

import pyautogui as pa
import keyboard as kb
import os
import time
import pywinauto as pw
import pygetwindow as gw
import getpass

from bs4 import BeautifulSoup as bs
from selenium import webdriver

from twilio.rest import Client
user=getpass.getuser()
os.chdir('C:/Users/'+user+'/OneDrive/util/overnight')
path='C:/Users/'+user+'/OneDrive/util/chromedriver.exe'
url='https://www.youtube.com/watch?v=1_dpGP5wOO0'
cf=0.85

sid='ACfcc99664b89dbc225561f7000a836305'
token='10b15278cbe5a2f242ad254686ceb341'
client=Client(sid, token)

absents_=pa.locateAllOnScreen('absent.png', confidence=cf)
absents=[absent for absent in absents_]
errors_XY=0
errors_call=0
XY_0=pa.locateOnScreen('phone_vertex.png')
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

    #이것은 전화가 온 것을 직접 감지한 것
    if pa.locateOnScreen('phonecall.png', confidence=cf) or pa.locateOnScreen('phonedis.png', confidence=cf) \
            or pa.locateOnScreen('phonecall2.png', confidence=cf) or pa.locateOnScreen('phonecall_bobath.png', confidence=cf):
        driver = webdriver.Chrome(path)
        driver.implicitly_wait(10)
        driver.get(url)
        driver.implicitly_wait(10)
        pa.click(pa.locateOnScreen('play_yt.png', confidence=cf))
        message = client.messages \
            .create(body='전화왔어요', from_='+19204770393', to='+821083782358')
        #message = client.messages \
        #    .create(body='전화왔어요 그 사람에게 알려주세요', from_='+19204770393', to='+821088777317')
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to='+821083782358',
            from_='+19204770393'
        )
        print(f'전화가 감지되었습니다. {time.strftime("%H:%M:%S",time.localtime(time.time()))}')
        time.sleep(60)

    #부재중 전화도 감지해야할 것이다
    else:
        if int(time.strftime('%H', time.localtime(time.time())))<24:
            xy = pa.position()
            absents_new_=pa.locateAllOnScreen('absent.png', confidence=cf)
            absents_new=[absent for absent in absents_new_]
            if not pa.locateOnScreen('call.png', confidence=cf):
                errors_call+=1
                if errors_call>5:
                    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+821083782358',
                        from_='+19204770393'
                    )
                else:
                    print('전화 기록 최상단으로 이동합니다')
                    pa.moveTo(XY_0[0] + 200, XY_0[1] + 500)
                    pa.scroll(5000)
            elif pa.locateOnScreen('call_absent.png'):
                message = client.messages \
                    .create(body='부재중 전화가 늘어났다', from_='+19204770393', to='+821083782358')
                call = client.calls.create(
                    url='http://demo.twilio.com/docs/voice.xml',
                    to='+821083782358',
                    from_='+19204770393'
                )
            elif absents_new!=absents:
                message = client.messages \
                    .create(body='부재중 전화가 늘어난 것 같다', from_='+19204770393', to='+821083782358')
                absents=absents_new
            else:
                pass

            if pa.locateOnScreen('phone_vertex.png') or pa.locateOnScreen('phone_vertex2.png'):
                #폰 모서리가 좌상, 우하단 다 보이는가? 안 보이면 오류 보고 하고, 보이면 화면 안 꺼지게 조치
                XY=pa.locateOnScreen('phone_vertex.png')
                XY_=pa.locateOnScreen('phone_vertex2.png')
                if XY is None:
                    errors_XY+=1

                    pa.moveTo(XY_0[0] + 200, XY_0[1] + 500)
                    pa.scroll(-500)
                    time.sleep(0.03)
                    pa.scroll(500)
                    if errors_XY>30:
                        call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+821083782358',
                            from_='+19204770393'
                        )
                    else:
                        message = client.messages \
                            .create(body='왼쪽 위 모서리가 가려졌다.', from_='+19204770393', to='+821083782358')
                elif XY_ is None:
                    errors_XY += 1
                    if errors_XY>30:
                        call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+821083782358',
                            from_='+19204770393'
                        )
                    else:
                        message = client.messages \
                            .create(body='오른쪽 아래 모서리가 가려졌다.', from_='+19204770393', to='+821083782358')
                else:
                    pa.moveTo(XY[0] + 200, XY[1] + 500)
                    pa.scroll(-500)
                    time.sleep(0.03)
                    pa.scroll(500)
            else:
                print("폰 모서리가 가려졌어요")
                errors_XY += 1
                if errors_XY > 30:
                    call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+821083782358',
                        from_='+19204770393'
                    )
                else:
                    message = client.messages \
                        .create(body='모서리가 가려졌다.', from_='+19204770393', to='+821083782358')
            pa.moveTo(xy)
            print(f'지금 시간은.... {time.strftime("%H:%M:%S", time.localtime(time.time()))}')
            time.sleep(20)
        else:
            print(f'퇴근하자')
            break