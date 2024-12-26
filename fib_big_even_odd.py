# 1.5. Определение четности n-го большого числа Фибоначчи
def fib_eo(n):
    if int(n) == 0:
        return "even"
    array = [0, 1]

    if 1 <= int(n) <= 10**6:
        for i in range(2, int(n) + 1):
            array.append(array[-1] + array[-2])
        return "even" if array[-1] % 2 == 0 else "odd", array[-1]
    else:
        raise ValueError("Число n должно быть в диапазоне 1 <= n <= 40")

n = input('Введите число: ')
result = fib_eo(n)
print(f"Фисло Фибоначчи {n} - {result}")


