# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, введя переключение цветов в отдельном потоке (С помощью класса Threads)
# и реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
# Подсказка: Подтверждения переключение можно показать вызовом print(self.color)
# через заданные промежутки времени для каждого цвета.
from color import Color
import threading
import time
import sys


def init_colors():
    red = Color("red", 7)
    green = Color('green', 5)
    yellow_form_red = Color('yellow', 2)
    yellow_from_green = Color('yellow', 4)
    red.next = yellow_form_red
    yellow_form_red.next = green
    green.next = yellow_from_green
    yellow_from_green.next = red
    return red


class TrafficLight:
    def __init__(self, color):
        self.__current = color

    def turn_on(self):
        self.run()
        while True:
            q = input()
            if q == 'q':
                sys.exit(0)

    def run(self):
        x = threading.Thread(target=self.running, args=(self.__current,), daemon=True)
        x.start()

    def running(self, color):
        print(f"{color.color} is running, enter q if you want to exit")
        time.sleep(color.wait)
        self.__current = color.next
        self.run()


startFrom = init_colors()
trafficLight = TrafficLight(startFrom)
trafficLight.turn_on()
