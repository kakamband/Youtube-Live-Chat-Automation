import json
from tkinter import Tk
import time
import pyautogui
import webbrowser
pyautogui.PAUSE=1
pyautogui.FAILSAFE=1


webbrowser.open('https://www.youtube.com/watch?v=xW78rDY-v2o')
time.sleep(10)

pyautogui.hotkey('ctrl','shift','i')
time.sleep(30)
pyautogui.click(860,169)

pyautogui.click(860,142)

pyautogui.typewrite('get_live')

pyautogui.click(794,189)

if (pyautogui.locateOnScreen('check3.png',region=(73,500,353,30),confidence=0.8) is None):
    pyautogui.click(794,245)


time.sleep(3)
pyautogui.click(1356,272)


# ----------------

while True:
    if (pyautogui.locateOnScreen('check.png',region=(797,204,250,100),confidence=0.8) is not None) or (pyautogui.locateOnScreen('check1.png',region=(797,204,250,100),confidence=0.8) is not None):
        print("yes")
        pyautogui.click(883,253)
        break
    else:
        print("no")
        time.sleep(3)

counter=0
lso=0
names=dict()

time.sleep(30)

while True:
    pyautogui.click(1153,228)
    pyautogui.click(1265,423)
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    clipboard = Tk().clipboard_get()
    tempname=[]
    try:
        clipboard=json.loads(clipboard)
        def myprint(d):
            for k, v in d.items():
                if isinstance(v, dict):
                    myprint(v)
                elif isinstance(v,list):
                    for i in v:
                        try:
                            i=json.dumps(i)
                            x=i.find('simpleText": "')
                            if x!=-1:
                                c=i[x+14:]
                                rname=c[:c.find('"},')]
                                names[rname]=time.time()
                                tempname.append(rname)
                        except Exception as e:
                            print(e)
                else:
                    pass

        myprint(clipboard)
        for i in tempname:
            vals=names[i]
            if time.time()-vals > 50:
                names[i]=time.time()
                print(i)
                pyautogui.click(163,519)
                if (pyautogui.locateOnScreen('check2.png',region=(73,500,353,30),confidence=0.8) is not None):
                    time.sleep(23)
                pyautogui.typewrite(f"Shoutout to {i}.Thanks for joining the stream.Love you guys.<3")
                pyautogui.press('enter')
                time.sleep(4)
            
        if (pyautogui.locateOnScreen('arrow.png',region=(935,240,30,30),confidence=0.8) is not None):
            for _ in range(10):
                pyautogui.click(947,262, button='left')
        else:
            time.sleep(3)
        
        pyautogui.click(883,253)
        counter+=1
        for counters in range(counter):
            pyautogui.press('down')
        lso+=1
    except:
            time.sleep(5)

