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

for index in range(0, len(array)):
    try:
        array[index] = int(input(f"Enter value for index - {index}: "))
    except:
        array[index] = -1
    if index % 2 != 0:
        array[index - 1], array[index] = array[index], array[index - 1]

print(array)
