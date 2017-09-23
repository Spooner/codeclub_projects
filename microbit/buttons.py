from microbit import *

display.show(Image.HEART)
while True:
    if button_a.is_pressed():
        display.show(Image.SQUARE)
    elif button_b.is_pressed():
        display.show(Image.HAPPY)
        