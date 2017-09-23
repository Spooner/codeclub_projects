from microbit import *

import speech

display.show(Image.HAPPY)
sleep(500)
display.show(Image("00000:09090:00000:09990:09990"))
speech.say("Hello, world!", pitch=64, speed=72, mouth=128, throat=128)
display.show(Image.HAPPY)
