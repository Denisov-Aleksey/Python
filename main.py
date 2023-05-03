# #12345 пример
# x = int(input())
# a = x // 10000
# b = x // 1000 % 10
# c = x // 100 % 10
# d = x // 10 % 10
# e = x % 10
# print(a, b, c, d, e)

# schoolboy = int(input())
# appels = int(input())
# number_of_apples = appels // schoolboy
# print(number_of_apples)

# schoolboy = int(input())
# appels = int(input())
# number_of_apples = appels % schoolboy
# print(number_of_apples)

# x = int(input())
# y = x % 10
# print(y)

# x = int(input())
# y = x // 10 % 10
# print(y)

# x = int(input())
# print((x // 100) + (x // 10 % 10) + (x % 10))

# from math import ceil
#
# n = int(input())
# m = int(input())
# print(ceil(m / n))


# a = int(input())  # рубли
# b = int(input())  # копейки
# n = int(input())  # пирожки
# coast = (a * 100 + b) * n
# print(coast // 100, coast % 100)

# следующие чётное
# a = int(input())
# print((a + 2) - (a % 2))

# Проверка на положительность
# x = int(input())
# print (x >= 0)

# Проверка на чётность
# x = int(input())
# print (x % 2 == 0)

# # Проверка на кратность 6
# x = int(input())
# print (x % 6 == 0)

# число не крано 9
# x = int(input())
# print (x % 9 > 0)

# # Последняя цифра числа 2 ?
# x = int(input())
# print (x % 10 == 2)

# # Оба числа деляться на 7
# x = int(input())
# y = int(input())
# print(x % 7 == 0 and y % 7 == 0)

# #Правильные треугольник
# a = int(input())
# b = int(input())
# c = int(input())
# print (a == b and b ==c and a ==c)

# # число двузначеное
# x = int(input())
# print(x >= 10 and x <= 99)


# Программа должна обьеденить два названия блюда в одно

# print("Введите название двух блюд: \n")
# food_name1 = input("Первое блюдо: ")
# food_name2 = input("Второе блюдо: ")
# print("Ваше новое невиданное блюдо", food_name1[0:4] + food_name2[2:10])

# щедрый посетитель

# count = int(input("Введите сумму счёта: "))
# tip_1 = count // 100 * 15
# tip_2 =count // 100 * 20
# print(" 15% Чаевых =", tip_1, "\n",
#       "20% Чаевых =", tip_2,)

# Автодиллер

# car_price = int(input("Введите цену автомобиля: "))
# tax = car_price // 100 * 13
# registration = car_price // 100 * 15
# agent_fee = 50000
# delivery = 100000
# finish_price = car_price + tax + registration + agent_fee + delivery
# print("Цена автомобиля в вашем городе",finish_price)


# n = list(map(int, input().split()))
# n.sort()
# a = n[0] 1
# b = n[1] 4
# c = n[2] 7
# print((b - a) + (c - b))

# a, b, c = input().split()
# a = f'''Simvol code {a} is {ord(a)}.'''
# b = f'''Simvol code {b} is {ord(b)}.'''
# c = f'''Simvol code {c} is {ord(c)}.'''
# print(a, b, c, sep="\n")

# a = input().lower()
# a = a.replace("o","").replace('e','').replace('a','')
# a = a.replace('y','').replace('i','').replace('u','')
# a = list(a)
# a = ".".join(a)
# a = "." + a
# print(a)
# a, b, c = int(input()), int(input()), int(input())
# a = hex(a)[2:].upper().zfill(2)
# b = hex(b)[2:].upper().zfill(2)
# c = hex(c)[2:].upper().zfill(2)
# print("#" + a + b + c)


# person = input().split()
# per_name = person[0][0].capitalize() + '.'
# sur_name = person[2].capitalize()
# mid_name = person[1][0].capitalize() + '.'
# text = f'{sur_name} {per_name}{mid_name}'
# print(text)

# person = input().split()
# text = f"{person[2]} {person[0][0]}.{person[1][0]}."
# print(text)

a = input().split()
b = '\n'.join(a)
print(b)
