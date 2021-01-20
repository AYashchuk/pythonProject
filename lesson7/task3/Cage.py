class Cage:
    def __init__(self, amount=0):
        self.__amount = amount if amount > 0 else 0

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        self.__amount = amount if amount > 0 else 0

    def __add__(self, other):
        return Cage(amount=(self.amount + other.amount))

    def __sub__(self, other):
        if other.amount <= other.amount:
            print("Cage's cant be subtracted")
            return None
        return Cage(amount=(self.amount - other.amount))

    def __mul__(self, other):
        return Cage(amount=(self.amount * other.amount))

    def __truediv__(self, other):
        return Cage(amount=round(self.amount / other.amount))

    def make_order(self, count_in_row):
        rows = self.amount // count_in_row
        rest = self.amount % count_in_row
        result = ''
        for i in range(0, rows):
            result += f"{''.ljust(count_in_row, '*')}\n"
        result += ''.ljust(rest, '*')
        return result
