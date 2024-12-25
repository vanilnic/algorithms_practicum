# 1.4. Вычисление n-го числа Фибоначчи при помощи формулы Бине
import math

def fib(n):
    if 1 <= int(n) <= 64:
        s_5 = math.sqrt(5)
        a = (1 + s_5) / 2
        b = (1 - s_5) / 2
        result = (a**int(n) - b**int(n)) / s_5
        return round(result)
    else:
        raise ValueError("Число n должно быть в диапазоне 1 <= n <= 64")


n = input('Введите число: ')
result = fib(n)
print(f"Число Фибоначчи({n}) = {result}")
