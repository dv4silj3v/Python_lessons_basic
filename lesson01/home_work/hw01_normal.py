
__author__ = 'Dmitry V. Vasilyev'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

number = str(input("Please enter the random number:"))

maxnum = '0'

for i in number:
    if i > maxnum:
        maxnum = i

print("The largest numeral in the number:", maxnum)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

variables = (int(input('Enter Variable A:')),int(input('Enter Variable B:')))

(a,b)= variables

a,b=b,a

print("Variable A:", a, " Variable B:", b)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math
import cmath

print("Please enter coefficients of a quadratic equation ax² + bx + c = 0")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
x1 = ''
x2 = ''
if a != 0:
    # Discriminant of the equation
    delta = (b**2) - (4 * a * c)
    if delta == 0:
        x1 = -(b / (2 * a))
        x2 = x1
        print("Discriminant is zero, x1=x2=", x1)
    elif delta >= 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Discriminant is positive, x1=", x1, " x2=", x2)
    else:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)
        print("Discriminant is negative, solution with imaginary units, x1=", x1, " x2=", x2)
else:
    print("This is not a quadratic equation!")