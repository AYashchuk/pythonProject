from Stationery import Stationery


class Handle(Stationery):
    def __init__(self):
        super().__init__('Handle')

    def draw(self):
        print(f"Зпуск отрисовки для {self._title}")
