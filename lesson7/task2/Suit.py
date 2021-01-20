from Clothes import Clothes


class Suit(Clothes):
    def __init__(self, h=0):
        super().__init__(h=h, name="Suit")

    def _count_expenses(self):
        return 2 * self.h + 0.3
