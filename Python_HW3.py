from random import randint

# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def Task1():
    my_list = [2, 3, 5, 9, 3]
    result = 0
    for i in range(1, len(my_list), 2):
        result += my_list[i]
    print(f"{my_list} -> сумма элементов на нечётных позициях: {result}")


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];  - [2, 3, 5, 6] => [12, 15]

def Task2():
    number = int(input('Введите размер списка '))
    listOne = []
    listTwo = []

    for i in range(number):
        listOne.append(randint(0, 9))

    for i in range(len(listOne)):
        while i < len(listOne)/2 and number > len(listOne)/2:
            number = number - 1
            result = listOne[i] * listOne[number]
            listTwo.append(result)
            i += 1

    print(listOne)
    print(listTwo)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def Task3():
    my_list = [1.1, 1.2, 3.1, 5, 10.01]
    new_list = [round(index % 1, 2) for index in my_list if index % 1 != 0]
    result = max(new_list) - min(new_list)
    print(f'Разница между максимальной и минимальной дробной частю = {result}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def Task4():
    num = int(input("Введите число: "))
    numprint = num
    result = " "
    while num != 0:
        result = str(num % 2) + result
        num //= 2
    print(f'{numprint} в двоичной -> {result}')



# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def Fibonacci(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def NegaFibonacci(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

def Task5():
    my_list = [0]
    numberU = int(input('Введите число: '))
    for indexI in range(1, numberU + 1):
        my_list.append(Fibonacci(indexI))
        my_list.insert(0, NegaFibonacci(indexI))
    print(my_list)




# __________________________________________________________________________________________
# ___________________________Блок вызова____________________________________________________
# __________________________________________________________________________________________

# Task1()
# Task2()
# Task3()
# Task4()
# Task5()