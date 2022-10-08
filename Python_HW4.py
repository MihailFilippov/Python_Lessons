from random import randrange, randint

# 1. Вычислить число c заданной точностью d


def input_numbers():
    while True:
        num = input('Введите число: ')
        try:
            number = float(num)
            return number
        except:
            print('Вы ввели не число. Попробуйте снова.')


def input_count():
    while True:
        num = input('Введите точность округления: ')
        try:
            numbers = int(num)
            return numbers
        except:
            print('Вы ввели не число. Попробуйте снова.')


def Task1():
    number = input_numbers()
    count = input_count()
    print(f'{number:.{count}f}')


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Task2():
    import math
    NUM = 26

    def prime_factors(inp_num):
        res_list = []
        while inp_num % 2 == 0:
            res_list.append(2)
            inp_num = inp_num / 2
        for i in range(3, int(math.sqrt(inp_num)) + 1, 2):
            while inp_num % i == 0:
                res_list.append(i)
                inp_num = inp_num / i
        if inp_num > 2:
            res_list.append(int(inp_num))
        return res_list
    print(prime_factors(NUM))


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def Task3():
    random_list = [randrange(1, 10) for _ in range(20)]
    print(random_list)
    random_list = set(random_list)
    print(random_list)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

def Task4():
    num = int(input("Введите натуральную степень k: "))

    def magit_to_file(num: int):
        if num > 0:
            num1 = randint(0, 100)
            str_1 = f"{num1}*x^{num}"
            for i in reversed(range(2, num)):
                num1 = randint(0, 100)
                if num1 != 0:
                    str_1 += f" + {num1}*x^{i}"
            num1 = randint(0, 100)
            if num1 != 0:
                str_1 += f" + {num1}*x"
            num1 = randint(0, 100)
            if num1 != 0:
                print(f"{str_1} + {num1} = 0")
            else:
                print(f"{str_1} = 0")
    magit_to_file(num)


# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# --------------простите, не успеваю, болею---------------------

# Task1()
# Task2()
# Task3()
Task4()