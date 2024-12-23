#1.1. Вычисление n-го числа Фибоначчи с использованием рекурсивного алгоритма
import time

def fib(n):
    if int(n) == 0:
        return 0
    elif int(n) == 1:
        return 1

    if 1 <= int(n) <= 24:
        return fib(int(n) - 1) + fib(int(n) - 2)
    else:
        raise ValueError("Число n должно быть в диапазоне 1 <= n <= 24")

n = input('Введите число: ')

try:
    start_time = time.time()
    result = fib(n)
    end_time = time.time()

    print(f"Число Фибоначчи {n}: {result}")
    print(f"Время выполнения алгоритма: {end_time - start_time:.6f} секунд")
except ValueError as e:
    print(f"Ошибка: {e}")

# замерить время выполнения алгоритма с точностью до миллисекунды любым доступным способом для пяти произвольных n
test_values = [5, 10, 15, 20, 24]
for n in test_values:
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    print(f"fib({n}) = {result}, время выполнения: {(end_time - start_time) * 1000:.3f} мс")