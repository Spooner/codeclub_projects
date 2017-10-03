#!/usr/bin/env python3

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from gpiozero import Servo

VERSION = '0.0.1'


class Car(Widget):
    left_button = ObjectProperty(None)
    right_button = ObjectProperty(None)
    forwards_button = ObjectProperty(None)
    backwards_button = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._left = Servo(17)
        self._right = Servo(18)

        self.stop()

    def rotate_left(self, *args):
        self._left.max()
        self._right.min()

    def rotate_right(self, *args):
        self._left.min()
        self._right.max()

    def move_forwards(self, *args):
        self._left.max()
        self._right.max()

    def move_backwards(self, *args):
        self._left.min()
        self._right.min()

    def stop(self, *args):
        self._left.mid()
        self._right.mid()


class CarApp(App):
    def build(self):
        car = Car()
        return car


if __name__ == '__main__':
    Builder.load_file("car.kv")
    CarApp().run()

