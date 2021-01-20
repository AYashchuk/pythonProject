# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации
# операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


from Matrix import Matrix

matrix1 = Matrix(3, 3, True)
matrix2 = Matrix(3, 3, True)
print('Matrix 1:')
print(matrix1)
print('Matrix 2:')
print(matrix2)
print('multiplied:')
multiplied_matrix = matrix1.multiply_matrix(matrix2)
print(multiplied_matrix)
