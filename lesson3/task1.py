# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


def divide(arg1, arg2):
    if arg2 == 0:
        return math.inf # of float('inf')
    else:
        return arg1 / arg2


print(divide(a, b))
