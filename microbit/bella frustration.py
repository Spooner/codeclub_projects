from microbit import *

while True:
    if pin0.read_digital():
        display.show(Image.SAD)
        sleep(20)
        display.show(Image.FROWN)
        sleep(20)
    else:
        display.show(Image.HEART)
        sleep(40)
    