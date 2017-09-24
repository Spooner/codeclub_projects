# https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/python-code
# https://github.com/adafruit/Adafruit_Python_CharLCD
# https://pimylifeup.com/raspberry-pi-lcd-16x2/
# $ pip3 install Adafruit_CharLCD

from subprocess import check_output
from time import sleep
from datetime import datetime

from Adafruit_CharLCD import Adafruit_CharLCD as LCD

# Interface could be eth0, wlan0, wlan1, etc.
CMD = "ip addr show wlan0 | grep inet | awk '{print $2}'"


def get_ip_addr():
    ip_addrs = check_output(CMD, shell=True, universal_newlines=True).strip().split("\n")
    ip_addr = ip_addrs[0].split("/")[0]
    return ip_addr


def get_now():
    now = datetime.now().strftime('%b %d - %H:%M:%S')
    return now


lcd = LCD(rs=5, en=6,  # LCD #4 and #6, respectively
          d4=22, d5=23, d6=24, d7=25, # LCD pins #11, #12, #13, #14
          cols=16, lines=2)
# Connect potentiometer to #3 (V0) for backlight brightness control.
# #15 and #16 power the backlight (5V and GND, respectively)

while True:
    lcd.clear()
    #lcd.home()
    #lcd.set_cursor(0, 0)
    lcd.message('{now}\nIP {ip_addr}'.format(now=get_now(), ip_addr=get_ip_addr()))
    sleep(1)
