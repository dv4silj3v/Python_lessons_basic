#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Cards:
    # Define our card
    def __init__(self):
        self.card = [[], [], []]

    def num_gen(self):
        # Generate matrix of numbers and sort each row
        self.card = [sorted([random.randint(1, 90) for x in range(9)]) for y in range(3)]

        # Popup four random numbers in each row
        for i, row in enumerate(self.card):
            randlist = []
            popnum = 4
            while popnum > 0:
                rannum = random.randint(0, 8)
                if rannum not in randlist:
                    randlist.append(rannum)
                    popnum -= 1
            for j, elem in enumerate(row):
                if j in randlist:
                    self.card[i][j] = str(" ")
        return self.card

    # Make a good looking output
    def __str__(self):
        return '\n'.join('{}'.format(row) for row in self.card)

    # Checking if number is on the card
    def num_check(self, number):
        for i, row in enumerate(self.card):
            for j, elem in enumerate(row):
                if number == elem:
                    return True
        return False

    # Crossing the number on the card
    def cross_num(self, number):
        for i, row in enumerate(self.card):
            for j, elem in enumerate(row):
                if number == elem:
                    self.card[i][j] = str(" ")
                    return True
        return False

    # Checking if the card has any numbers left
    def card_check(self):
        return len([column for row in self.card for column in row if type(column) == int]) > 0


class LottoGame:
    def __init__(self, player_card, cpu_card):
        self.player_card = player_card
        self.cpu_card = cpu_card
        self.barrels = []

    def _show_stat(self, i, barrel):
        print("New Barrel: {}. Barrels left: {}".format(barrel, len(self.barrels) - i - 1))
        print("------ Player Card -------")
        print(self.player_card)
        print("--------------------------")
        print("------ CPU Card ----------")
        print(self.cpu_card)
        print("--------------------------")

    def _player_turn(self, barrel):
        while True:
            answer = input("Cross the number? (Y/N)")
            if answer == 'Y':
                if not self.player_card.cross_num(barrel):
                    print("Number is not on card. You lost..")
                    exit()
                break
            elif answer == 'N':
                if self.player_card.cross_num(barrel):
                    print("Number is on the card. You lost..")
                    exit()
                break
            elif answer == 'q':
                exit()

    def _cpu_turn(self, barrel):
        if self.cpu_card.num_check(barrel):
            print("CPU crossed number {}".format(barrel))
            self.cpu_card.cross_num(barrel)
        else:
            print("CPU didn't cross number: {}".format(barrel))

    def _check_victory_conditions(self):
        if not self.player_card.card_check() and not self.cpu_card.card_check():
            print("It's a DRAW!")
            return True
        elif not self.player_card.card_check():
            print("You Lost!")
            return True
        elif not self.cpu_card.card_check():
            print("You won!")
            return True
        return False

    def start_game(self):
        self.barrels = random.sample(range(1, 91), 90)
        print("Welcome to the Lotto Game!!")
        for i, barrel in enumerate(self.barrels):
            self._show_stat(i, barrel)
            self._player_turn(barrel)
            self._cpu_turn(barrel)
            if self._check_victory_conditions():
                return


player_card = Cards()
player_card.num_gen()
cpu_card = Cards()
cpu_card.num_gen()

lotto = LottoGame(player_card, cpu_card)
lotto.start_game()






