
__author__ = 'Dmitry V. Vasilyev'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# код пишем тут...
number = str(input('Please enter the random number:'))

print('Number consists of following numerals:')
for i in number:
    print(i)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

var_a = int(input("Enter the variable A:"))
var_b = int(input("Enter the variable B:"))
var_c = var_a + var_b

for i in [var_a, var_b]:
    if i == var_a:
        print("Variable A:",var_c - i)
    else:
        print("Variable B:",var_c - i)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input('What is your age'))

if age >= 18:
    print("Access granted")
else:
    print("Sorry, access can be granted for users above 18 years old")