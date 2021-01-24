# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


try:
    isRunning = True
    with open("file.dat", "w") as f_obj:
        while isRunning:
            text = input('Enter text: ')
            if text is not '':
                f_obj.write(text + '\n')
            else:
                isRunning = False
except IOError:
    print("Произошла ошибка ввода-вывода!")
