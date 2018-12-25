# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):

    row = [1, 1]
    for j in range(n, m):
        x, y = 1,1
        for i in range(1, j):
            x, y = y, x + y
        row.append(y)
    return row[n:]

print(fibonacci(2, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):

    for i in range(1, len(origin_list)):
        index = origin_list[i]
        j = i - 1
        while j >= 0 and index < origin_list[j]:
            origin_list[j + 1] = origin_list[j]
            j = j - 1
            origin_list[j + 1] = index
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

import math

def superfilter(f, var):
    return [i for i in var if f(i)]

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(superfilter(lambda x: math.sqrt(x) - int(math.sqrt(x)) == 0, numlist))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import decimal
decimal.getcontext().prec = 10

class Vector2d:
    x = decimal.Decimal(0)
    y = decimal.Decimal(0)
    def __init__(self, x, y):
        self.x = decimal.Decimal(x)
        self.y = decimal.Decimal(y)
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)
    def normalize(self):
        d = (self.x * self.x + self.y * self.y).sqrt()
        self.x /= d
        self.y /= d

def dot(v1, v2):

    return v1.x * v2.x + v1.y * v2.y

def is_parallel(v1, v2):

    v1.normalize()
    v2.normalize()
    r = dot(v1, v2)
    return r == 1 or r == -1


a1 = Vector2d(1, 0)
a2 = Vector2d(4, 0)
a3 = Vector2d(-1, -1)
a4 = Vector2d(2, -1)

v1 = a2 - a1
v2 = a4 - a3
v3 = a3 - a1
v4 = a4 - a2

print(is_parallel(v1, v2))
print(is_parallel(v3, v4))