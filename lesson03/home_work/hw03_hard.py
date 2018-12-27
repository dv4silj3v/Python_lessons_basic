# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def fractions(expression):
    # Basic check that expression is a simple string:
    if type(expression) != str:
        print('Thats not a right expression with fractions')
    # Let's split expression into small pieces and find numerator and denominator
    expr_quant = expression.split(' ')

    if '/' not in expr_quant[0]:
        a = expr_quant[0]
        b = 1
    else:
        a, b = expr_quant[0].split('/')

    if '/' not in expr_quant[2]:
        c = expr_quant[2]
        d = 1
    else:
        c, d = expr_quant[2].split('/')

    if expr_quant[1] == '+':
        expr_numerator = int(a) * int(d) + int(c) * int(b)
    else:
        expr_numerator = int(a) * int(d) - int(c) * int(b)

    expr_denominator = int(b) * int(d)

    if expr_numerator < expr_denominator:
        expr_numerator_out, expr_denominator_out = expr_numerator, expr_denominator
        if expr_numerator < 0:
            expr_numerator = -expr_numerator
        while expr_numerator != 0 and expr_denominator != 0:
            if expr_numerator > expr_denominator:
                expr_numerator = expr_numerator % expr_denominator
            else:
                expr_denominator = expr_denominator % expr_numerator
        gds = expr_numerator + expr_denominator

        print(int(expr_numerator_out/gds),'/', int(expr_denominator_out/gds))
    elif expr_numerator == expr_denominator:
        print(expr_numerator/expr_denominator)
    else:
        if expr_numerator < 0:
            expr_numerator = -expr_numerator
        expr_numerator_out, expr_denominator_out = expr_numerator, expr_denominator
        while expr_numerator != 0 and expr_denominator != 0:
            if expr_numerator > expr_denominator:
                expr_numerator = expr_numerator % expr_denominator
            else:
                expr_denominator = expr_denominator % expr_numerator
        gds = expr_numerator + expr_denominator

        print(int(expr_numerator_out//expr_denominator_out), int(expr_numerator_out%expr_denominator_out / gds), '/', int(expr_denominator_out / gds))


fractions('-9/5 - 1/8')


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os
import json

DIR = 'data'

statement = []
hours_out = []
line_column = []
payroll = []

with open(os.path.join(DIR, 'workers'), 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        if i >= 1:
            line_column = line.strip('\n').split()
            statement.append({'Name:':line_column[0], 'Surname:':line_column[1], 'Salary:':line_column[2], 'Title:':line_column[3], 'HPM:':line_column[4]})

with open(os.path.join(DIR, 'hours_of'), 'r', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        if i >= 1:
            line_column = line.strip('\n').split()
            hours_out.append({'Name:':line_column[0], 'Surname:':line_column[1], 'HW:':line_column[2]})

for j in hours_out:
    for i in statement:
        if j["Surname:"] == i["Surname:"] and j["Name:"] == i["Name:"]:
            if int(i["HPM:"]) >= int(j["HW:"]):
                salary = int(i["Salary:"]) * int(j["HW:"]) / int(i["HPM:"])
                payroll.append({"Name:":j["Name:"], "Surname:":j["Surname:"], "Salary:":salary})
            if int(i["HPM:"]) < int(j["HW:"]):
                salary = int(i["Salary:"]) + 2 * (int(i["Salary:"])/int(i["HPM:"])) * (int(j["HW:"]) - int(i["HPM:"]))
                payroll.append({"Name:": j["Name:"], "Surname:": j["Surname:"], "Salary:": salary})

with open(os.path.join(DIR, 'payroll.json'), 'w', encoding='UTF-8', ) as f:
    json.dump(payroll, f, ensure_ascii=False)



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

for j in list(map(chr, range(ord('А'), ord('Я')+1))):
    with open(os.path.join(DIR, 'fruits.txt'), 'r', encoding='UTF-8') as f:
        for i, line in enumerate(f):
            if j in line:
                fruit_file_name = 'fruits_' + j
                path = os.path.join('data', fruit_file_name)

                fruits = open(path, 'a+', encoding='UTF-8')
                fruits.write(line)
                fruits.close()