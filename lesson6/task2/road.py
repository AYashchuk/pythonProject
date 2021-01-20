class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate(self, weight, depth):
        return self.__width * self.__length * weight * depth
