from Stationery import Stationery


class Pen(Stationery):
    def __init__(self):
        super().__init__('Pen')

    def draw(self):
        print(f"Зпуск отрисовки для {self._title}")
