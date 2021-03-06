# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
          
# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
# First option:
print("matrix_rotate = ", list(map(list, zip(*matrix))))

# Second option:
print("matrix_rotate = ", [[matrix[i][j] for i, el in enumerate(line)] for j, line in enumerate(matrix)])

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
number = """
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

import re

num_lst = re.findall('\d', number)
i = len(num_lst)

mlpl_tmp = 1
mlpl = 1 # max multiplication
z = 1 # last index of the numbers
mlpl_lst = ''

while i > 4:
    for j in range(i-5, i):
        mlpl_tmp *= int(num_lst[j])
    if mlpl_tmp > mlpl:
        mlpl = mlpl_tmp
        z = i
    mlpl_tmp = 1
    i -= 1
print("Multiplication equals to: {}; index of the first digit is {}".format(mlpl, z-5))


# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

def input_queen():

    queen_pos = []

    while len(queen_pos) < 8:
        queen_pos_lst = [int(x) for x in input("Enter the queen position: ").split()]
        if len(queen_pos_lst) == 2 and \
                1 <= queen_pos_lst[0] <= 8 and \
                1 <= queen_pos_lst[1] <= 8 and \
                queen_pos_lst not in queen_pos:
            queen_pos.insert(i, queen_pos_lst)
            print(queen_pos)
        else:
            print("Incorrect position or position is already in use, number must be between 1 and 8, e.g. 2 5")
    return queen_pos

def queen_cross(queen_pos):

# Let's start with checking if any of the queens is in the same row/column:
    list_index_0 = [item[0] for item in queen_pos]
    list_index_1 = [item[1] for item in queen_pos]
    print(list_index_0, list_index_1)
    if len(list_index_0) > len(set(list_index_0)) or len(list_index_1) > len(set(list_index_1)):
        print("YES")
    for i, line in enumerate(queen_pos):
        for j, el in enumerate(line):
            print(i, j)

queen_cross(input_queen())