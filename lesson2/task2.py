# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

length = 2

try:
    length = int(input('Enter array length: '))
except:
    print('Entered value inst int type')

array = [0] * length
i = 0
while i < length:
    try:
        array[i] = int(input(f"Enter value for index - {i}: "))
    except:
        array[i] = -1
    if i % 2 != 0:
        array[i - 1], array[i] = array[i], array[i - 1]
    i += 1

print(array)
