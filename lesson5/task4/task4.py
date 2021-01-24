# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import re

numbers_map = {
    'One': "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре"
}

try:
    with open("file1.txt") as f_obj_r:
        with open("file2.txt", "w") as f_obj_w:
            for line in f_obj_r:
                value = re.split('—', line.rstrip())
                write_line = f"{numbers_map[value[0].strip()]} - {value[1].strip()}\n"
                f_obj_w.write(write_line)
except IOError:
    print("Произошла ошибка ввода-вывода!")
