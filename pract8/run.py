import re

#Задание 1. Написать регулярное выражение, определяющее, является ли строка кодом цвета в 16-ричном формате.
print("Задание 1")
print("Корректное значение" if re.match("#[0-9A-Fa-f]{3,6}$", input('Введите значение: ')) else "Некорректное значение")

#Задание 3. Написать регулярное выражение для проверки адреса IP4. 
# Проверку на превышение значений 255 включать не нужно.
print("Задание 3")
print("Корректное значение" if re.match("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", input('Введите значение: ')) else "Некорректное значение")

#Задание 9. Написать регулярное выражение, проверяющее строку на соответствие почтовому индексу в российском формате.
print("Задание 9")
print("Корректное значение" if re.match("^\d{6}$", input('Введите значение: ')) else "Некорректное значение")
