# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

listType = []
boolType = True
bytesType = bytes(0)
tupleType = (5, 'program', 1+3j)
setType = {1, 2, 3, 4, 5}
mapType = {'a': 1, 'b': 2}
errorType = ZeroDivisionError
targetList = [1, "a", boolType, bytesType, tupleType, setType, mapType, errorType, listType]

for val in targetList:
    print(type(val))
