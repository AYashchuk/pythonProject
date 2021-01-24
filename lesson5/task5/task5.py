# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
sum = 0

try:
    with open("file.dat", "w") as f_obj:
        for number in range(0, 300):
            f_obj.write(str(number) + ' ')

    f_obj = open("file.dat", "r")
    number = ''
    while True:
        content = f_obj.read(1)
        if content == ' ' or not content:
            try:
                sum += int(number)
                number = ''
            except:
                pass
        else:
            number += content
        if not content:
            break

    f_obj.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")

print(sum)