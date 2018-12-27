# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

init_lst = [random.randint(-10, 10) for _ in range(10)]

print('init_lst =', init_lst)

square_lst = [el**2 for el in init_lst]

print('square_lst =',square_lst)


# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruit_list1 = ["apple", "banana", "cherry", "watermelon", "pineapple"]
fruit_list2 = ["watermelon", "passion fruit", "peach", "cherry", "apple"]

fruit_list = [fruits for fruits in fruit_list1 if fruits in fruit_list2]

print('fruit_list =', fruit_list)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

init_lst = [random.randint(-100, 100) for _ in range(10)]

print('init_lst =', init_lst)

new_lst = [el for el in init_lst if el%3 == 0 if el>0 if el%4 != 0]

print('new_lst =', new_lst)