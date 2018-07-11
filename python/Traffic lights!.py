import unicornhathd as unicorn
from time import sleep

unicorn.rotation(180)
unicorn.brightness(0.75)

def light(x,y,r,g,b):
    unicorn.set_pixel(x,y,r,g,b)
    unicorn.set_pixel(x+1,y,r,g,b)
    unicorn.set_pixel(x+2,y,r,g,b)
    unicorn.set_pixel(x,y-1,r,g,b)
    unicorn.set_pixel(x+1,y-1,r,g,b)
    unicorn.set_pixel(x+2,y-1,r,g,b)
    unicorn.set_pixel(x+3,y-1,r,g,b)
    unicorn.set_pixel(x+3,y,r,g,b)
    unicorn.set_pixel(x,y-2,r,g,b)
    unicorn.set_pixel(x+1,y-2,r,g,b)
    unicorn.set_pixel(x+2,y-2,r,g,b)
    unicorn.set_pixel(x+3,y-2,r,g,b)
    unicorn.set_pixel(x,y-3,r,g,b)
    unicorn.set_pixel(x+1,y-3,r,g,b)
    unicorn.set_pixel(x+2,y-3,r,g,b)
    unicorn.set_pixel(x+3,y-3,r,g,b)
    
    
while True:
    #red
    unicorn.clear()
    light(6,15,255,0,0)
    unicorn.show()

    sleep(3)

    # red + amber
    unicorn.clear()
    light(6,15,255,0,0)
    light(6, 11, 254, 127, 0)
    unicorn.show()

    sleep(1)

    #green
    unicorn.clear()
    light(6, 7, 0, 255, 0)
    unicorn.show()

    sleep(3)

    #amber
    unicorn.clear()
    light(6, 11, 254, 127, 0)
    unicorn.show()

    sleep(1)
