# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    arguments = sorted(list(args), reverse=True)
    length = len(arguments)
    if length < 2:
        return 0 if length == 0 else arguments[0]
    else:
        print(arguments)
        return arguments[0] + arguments[1]


print(my_func(1, 2, 3))
