# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

#num = int(input("Введите день недели "))
# if num == 6 or num == 7:
#    print("выходной")
# else: print("не выходной")





# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            print(not (x or y or z) == (not x) and (not y) and (not z))





# 3. Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# x = int(input("Введите x "))
# y = int(input("Введите y "))
# if x == 0 or y == 0:
#     print("введите точки не равные 0")

# if x > 0:
#     if y > 0:
#         print("first quarter")
#     else:
#         print("second quarter")
# else:
#     if y > 0:
#         print("third quarter")
#     else:
#         print("fourth quarter")





# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# n = int(input('Введите номер четверти: '))
# if n < 1 or n > 4:
#     print('Пожалуйста, введите число в пределе от 1 до 4')
# elif n == 1:
#     print('x > 0 и y > 0')
# elif n == 2:
#     print('x < 0 и y > 0')
# elif n == 3:
#     print('x < 0 и y < 0')
# elif n == 4:
#     print('x > 0 и y < 0')





# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# print('Enter coordinates point А:')
# xA = float(input('X: '))
# yA = float(input('Y: '))
# print("Enter coordinates point B:")
# xB = float(input('X: '))
# yB = float(input('Y: '))

# from math import sqrt
# print('Расстояние между точками А и В: ',round(sqrt((xA - xB)**2 + (yA - yB)**2), 2))
