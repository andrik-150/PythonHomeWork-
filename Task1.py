'''задача 1.
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

6 -> да
7 -> да
1 -> нет'''

day = int(input("Введите число: "))
if day == 6 or day == 7:
    print("Да")
elif 1 <= day <= 5:
    print("Нет")
else:
    print('Некорректный ввод. Попробуйте снова')
