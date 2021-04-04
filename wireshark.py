#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import random
os.system("cls")
time.sleep(1)
import webbrowser
def open(qwe=0):
    while True:
        #MNASJKFNAKSDMAJKFBJA
        if qwe <100:
            print("[+] Wireshark network listener initializing {}%".format(qwe)

                                       )
            qwe+=random.randint(1,10)
            time.sleep(1)
        else:
            print("[+] Wireshark network listener initializing 100")
            os.system("cls")
            break
time.sleep(10)
open(qwe=0)
print("Wireshark network ağ trafiği dinleniyor")
pp = 0
for i in range(1,100):
    if pp !=100:
        time.sleep(10)
        os.system("cls")
        print("[!] Network listening {}%".format(pp))
        pp = pp + random.randint(1, 5)
    else:
        break
os.system("cls")
print("[+] İp found!")
time.sleep(10)
print("İp: 88.203.147.63")
print("[+] Location searching")
time.sleep(5)
for i in range(1, 100):
    if i != 100:
        os.system("cls")
        print("[+] Location searching /")
        os.system("cls")
        print("[+] Location searching |")
        os.system("cls")
        print("[+] Location searching \ ")
        os.system("cls")
        print("[+] Location searching -")
    else:
        time.sleep(2)
        break
print("[+] Location found!")
time.sleep(5)
print("Location: Mardin/Turkey")
time.sleep(10)
print("[+] Os found!")
time.sleep(5)
print("Os: Samsung GLXY s20 v11.0")
webbrowser.open("https://www.google.com/maps/place/37%C2%B019'33.1%22N+40%C2%B043'14.7%22E/@37.3258646,40.7207533,17z/data=!3m1!4b1!4m5!3m4!1s0x0:0x0!8m2!3d37.3258646!4d40.7207533",new=0,autoraise=True)
time.sleep(5)
print("Done :)")
