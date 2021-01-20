from Stationery import Stationery


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Pencil')

    def draw(self):
        print(f"Зпуск отрисовки для {self._title}")
