# 3. Узнайте у пользователя число n (число в диапазоне от 0 до 9 включительно).
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите число: "))
res = n + (n*100 + 10*n + n) + (n*10 + n)
print(res)