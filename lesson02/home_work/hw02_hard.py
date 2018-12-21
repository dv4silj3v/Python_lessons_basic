# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

def equat_solution(equation, x):
    # let's split our string into small pieces
    elems = []
    for i in equation.split(' '):
        elems.append(i)
    # finding k and b coefficients
    k = float(elems[2][:-1])
    b = float(elems[4])

    print("k is:", k, " b is:",b)

    y = k * x + b
    print("y = ", y)

equat_solution(equation, x)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

def month_validate(month):
    return 0 < month <= 12

def day_validate(day, month):
    months_list_l = [1, 3, 5, 7, 8, 10, 12] #31 day (long) months
    months_list_s = [2, 4, 6, 9, 11] #30 day (short) months

    if month in months_list_l:
        if day >= 1 and day <= 31:
            return True
        else:
            return False

    if month in months_list_s:
        if day >= 1 and day <= 30:
            return True
        else:
            return False

def year_validate(year):
    return 1 < year <= 9999


today = input("Please insert a date in format DD.MM.YYYY: ")
todayslist = list(map(int, today.split('.')))

if month_validate(int(todayslist[1])) and day_validate(int(todayslist[0]),int(todayslist[1])) and year_validate(int(todayslist[2])):
    print("Date is valid")
else:
    print("Date is incorrect")

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

# Defining a function that finds a room in the cube of floors
def get_room_cube(N):

    largest_room_of_cube = 0
    cube = 1
    highest_floor_of_cube = 0

# Let's find for a virtual cube of rooms and cube size
    while largest_room_of_cube < N:
        largest_room_of_cube = largest_room_of_cube + cube**2
        highest_floor_of_cube = highest_floor_of_cube + cube
        cube += 1
    cube = cube - 1

# Then we do a simple math calculations to find a room within a cube
    lowerest_floor_of_cube = highest_floor_of_cube - cube + 1
    smallest_room_of_cube = largest_room_of_cube - cube**2 + 1
    room_floor = lowerest_floor_of_cube + ((N - smallest_room_of_cube) // cube)
    room_position = (N - smallest_room_of_cube) % cube + 1

    print("Room is located on {} floor, it is {} from left ".format(room_floor, room_position))

get_room_cube(int(input("Please enter the room number: ")))
