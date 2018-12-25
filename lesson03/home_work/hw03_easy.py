# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    snumber = number * (10 ** ndigits)
    dot = len(str(int(snumber))) + 1
    if int(str(snumber)[dot]) > 5:
        snumber = snumber + 1
    return float(int(snumber) / (10 ** ndigits))

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    ndigits = []
    for i in str(ticket_number):
        ndigits.append(int(i))
    if len(ndigits) != 6:
        return False
    if sum(ndigits[:3]) == sum(ndigits[3:]):
        return True
    else:
        return False


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
