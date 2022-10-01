# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = input('Введите число: ')
# result = 0
# for index in num:
#     if index.isdigit():
#         result += int(index)
# print(result)


# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# def factorial(n, result=1):
#     for i in range(1, n + 1):
#         result *= i
#     return result

# n = int(input("Введите N "))
# b = []
# for i in range(1, n+1):
#     b.append(factorial(i))
# print(b)


# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input("Введите число"))
# my_list = [n, [round(((1+1/n)**n),2)] for n in range(1, n+1)]
# print("Последовательность чисел", dict(my_list))
# print("Сумма последовательностей чисел" ,sum(dict(my_list)))


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
# элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# f = open('file.txt', 'w')   # создание файла
# f.write('3\n')      # позиция 3
# f.write('8\n')      # позиция 8
# f.close()

# n = int(input("Введите число "))
# num = []
# number = []
# for i in range(-n, n + 1):
#     num.append(i)
# f = open('file.txt')
# n1 = int(f.read(1))
# n2 = int(f.read(2))
# mult = num[n1] * num[n2]
# print(
#     f'Массив -> {num}. Произведение элементов на позициях {n1} и {n2} -> {mult}')
# for i in range(len(num)):
#     number.append(i)
# f.close()


# 5. Реализуйте алгоритм перемешивания списка

# from random import randint

# my_list = [1, 2, 3, 4, 5, 6]
# for index_i in range(len(my_list)):
#     index_j = randint(0, len(my_list) - 1)
#     my_list[index_i],my_list[index_j] = my_list[index_j],my_list[index_i]
# print(my_list)
