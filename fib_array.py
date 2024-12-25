# 1.3. Вычисление n-го числа Фибоначчи с записью числового ряда в массив
def fib(n):
    array = [0, 1]

    if 1 <= int(n) <= 40:
        for i in range(2, int(n) + 1):
            array.append(array[-1] + array[-2])
        return array
    else:
        raise ValueError("Число n должно быть в диапазоне 1 <= n <= 40")

n = input('Введите число: ')
result = fib(n)
print(f"array({n}) = {result}")
