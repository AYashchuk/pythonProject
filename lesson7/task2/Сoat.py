from Clothes import Clothes


class Coat(Clothes):
    def __init__(self, v=0):
        super().__init__(v=v, name="Coat")

    def _count_expenses(self):
        return self.v / 6.5 + 0.5
