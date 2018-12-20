# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math

numberslist = [7, 25, 196, 144, 64, 32, 45, -2]
print("Initial list of number:", numberslist)

sqrtnumberslist = []

for i in numberslist:
    if i > 0:
        if math.sqrt(i) - int(math.sqrt(i)) == 0:
            sqrtnumberslist.append(i)
print("SQRT list of numbers", sqrtnumberslist)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

import calendar
import num2words

today = input("Please insert a date in format MM.DD.YYYY: ")

todayslist = list(map(int, today.split('.')))

print("{} the {}th of year {}".format(calendar.month_name[todayslist[0]], num2words.num2words(todayslist[1]), todayslist[2]))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

# Generating random numbers list length and numbers in it
n = random.randint(5,15)

i = 0
numberslist = []

while i <= n:
    numberslist.append(random.randint(-100,100))
    i += 1
print(numberslist)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = []
i = 0
n = int(input("Insert the array length: "))
while i <= n:
    lst.append(random.randint(0,10))
    i += 1
print("This is the source list of numbers: ", lst)

lst1 = list(set(lst))

lst2 = []
for j in lst:
    if lst.count(j) <= 1:
        lst2.append(j)

print("This is a list without duplicates: ", lst1)
print("This ia a list of numbers that don't have duplicates: ", lst2)