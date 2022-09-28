# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# num = input('Введите число: ')
# result = 0
# for i in num:
#     if i != '.':
#         result += int(i)
# print(result)


# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(n, result=1):
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Введите N "))
b = []
for i in range(1, n+1):
    b.append(factorial(i))
print(b)
