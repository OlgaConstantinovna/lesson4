# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

number = int(input("Введите число: "))
i = 2 
multiplier = []
old = number
while i <= number:
    if number % i == 0:
        multiplier.append(i)
        number //= i
    else:
        i += 1
print(f"Простые множители числа {old} приведены в списке: {multiplier}")


