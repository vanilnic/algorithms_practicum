#1.2. Вычисление n-го числа Фибоначчи с использованием цикла
import time

def fib(n):
    if int(n) == 0:
        return 0
    elif int(n) == 1:
        return 1

    fib0, fib1 = 0, 1
    if 1 <= int(n) <= 32:
        for _ in range(2, int(n) + 1):
            fib0, fib1 = fib1, fib0 + fib1
        return fib1
    else:
        raise ValueError("Число n должно быть в диапазоне 1 <= n <= 32")

n = input('Введите число: ')

try:
    start_time = time.time()
    result = fib(n)
    end_time = time.time()

    print(f"Число Фибоначчи {n}: {result}")
    print(f"Время выполнения алгоритма: {end_time - start_time:.6f} секунд")
except ValueError as e:
    print(f"Ошибка: {e}")

#замерить время выполнения алгоритма с точностью до миллисекунды любым доступным способом для пяти произвольных n
test_values = [5, 10, 20, 25, 32]
for n in test_values:
    start_time = time.time()
    result = fib(n)
    end_time = time.time()
    print(f"fib({n}) = {result}, время выполнения: {(end_time - start_time) * 1000:.3f} мс")