class ShouldBeIntegerError(ValueError):
    def __init__(self, txt):
        self.txt = txt


class Complex:
    def __init__(self, i=0, j=0):
        try:
            self.__i = self.validate_value(i)
            self.__j = self.validate_value(j)
        except ValueError as err:
            raise ShouldBeIntegerError('Value should be Number')

    @property
    def i(self):
        return self.__i

    @i.setter
    def i(self, i):
        try:
            self.__i = self.validate_value(i)
        except ValueError as err:
            raise ShouldBeIntegerError('Value should be Number')

    @staticmethod
    def validate_value(value):
        return float(value)

    @property
    def j(self):
        return self.__j

    @j.setter
    def j(self, j):
        try:
            self.__j = self.validate_value(j)
        except ValueError as err:
            raise ShouldBeIntegerError('Value should be Number')

    def __add__(self, other):
        return Complex(self.__i + other.i, self.__j + other.j)

    def __sub__(self, other):
        return Complex(self.__i - other.i, self.__j - other.j)

    def __mul__(self, other):
        newComplex = Complex()
        newComplex.i = self.__i * other.i - (self.__j * other.j)
        newComplex.j = self.__i * other.j + self.j * other.i
        return newComplex

    def __str__(self):
        return f"{self.i} + {self.j}j"


complex1 = Complex(-4, 0)
complex2 = Complex(2, 5)

complex_add = complex1 + complex2
complex_sub = complex1 - complex2
complex_mul = complex1 * complex2
print("Sum: ", complex_add)
print("Mul: ", complex_mul)
print("Sub: ", complex_sub)
