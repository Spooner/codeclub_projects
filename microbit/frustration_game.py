from microbit import *
import music

lives = 3
display.show(str(lives))
while lives > 0:
    if pin1.read_digital():
        display.show(Image.SAD)
        music.pitch(200, 800)
        lives -= 1
        display.show(str(lives))

SKULL = [
    '09990',
    '90909',
    '99999',
    '09990',
    '09990',
]

for i in range(5):
    display.show(Image(":".join(["00000"] * (4 - i) + SKULL[:i + 1])))
    sleep(500)
    
music.play(music.FUNERAL)

brightness = 9
direction = -1
while True:
    if brightness == 1:
        direction = +1
    elif brightness == 9:
        direction = -1
    brightness += direction

    display.show(Image(":".join(SKULL).replace("9", str(brightness))))
    sleep(200)
