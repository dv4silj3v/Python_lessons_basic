
__author__ = 'Dmitry V. Vasilyev'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True



# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?

# Let's define a simple function of a quadratic equation

# We will use unbounded upper value for this exercise
a = float("inf")

print("a==a**2:",a == a**2)
print("a==a*2:",a == a*2)
print("a>999999",a > 999999)

# Подсказка: это значение точно есть ;)
