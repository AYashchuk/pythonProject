from enum import Enum


class Color:
    def __init__(self, name, wait):
        self.__name = name
        self.__wait = wait
        self.__next = None

    @property
    def color(self):
        return self.__name

    @property
    def wait(self):
        return self.__wait

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_color):
        self.__next = next_color
