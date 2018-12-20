# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ['apple', 'banana', 'kiwi', 'watermelon']

for i in range(len(fruits)):
    print("{}. {:>10}".format(i+1, fruits[i]))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

fruits1 = ['apple', 'banana', 'kiwi', 'watermelon', 'mango']
fruits2 = ['banana', 'mango', 'watermelon', 'carrot', 'cabbage', 'onion']

fruits_basket = []

for i in fruits2:
    if i in fruits1:
        fruits_basket.append(i)
print("Fruit basket consists of:", fruits_basket)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

import random

# Generating random numbers list length and numbers in it
numberslistlength = random.randint(5,15)

i = 0
numberslist = []

while i <= numberslistlength:
    numberslist.append(random.randint(1,1000))
    i += 1
print(numberslist)

for j in range(len(numberslist)):
    if numberslist[j] % 2 == 0:
        numberslist[j] = numberslist[j] / 4
    else:
        numberslist[j] = numberslist[j] * 2

print(numberslist)