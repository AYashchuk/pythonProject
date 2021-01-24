# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


result = []
try:
    with open("file.txt") as f_obj:
        for line in f_obj:
            result.append(len(line.rstrip()))
except IOError:
    print("Произошла ошибка ввода-вывода!")

print(result)
for index, value in enumerate(result):
    print(f"line {index + 1}, length: {value}")
