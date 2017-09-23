from gpiozero import Servo
from time import sleep

class Robot:
    def __init__(self):
        self._left = Servo(17)
        self._right = Servo(18)

    def left(self):
        self._left.max()
        self._right.min()
        
    def right(self):
        self._left.min()
        self._right.max()
        
    def forward(self):
        self._left.max()
        self._right.max()
        
    def backward(self):
        self._left.min()
        self._right.min()
        
    def stop(self):
        self._left.mid()
        self._right.mid()
           
robot = Robot()
try:
    sleep(15) # So we can disconnect wires and put on the floor.
    
    while True:
        robot.left()
        sleep(1)
        robot.forward()
        sleep(1)
        robot.left()
        sleep(1)
        robot.forward()
        sleep(1)
        robot.left()
        sleep(1)
        robot.forward()
        sleep(1)
        robot.stop()
        sleep(5)
finally:    
    robot.stop()
   
