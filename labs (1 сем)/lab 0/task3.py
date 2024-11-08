import timeit

def last_digit_fib(n):
    if n <= 1:
        return n
    
    previous, current = 0, 1
    
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10
    
    return current

# Чтение числа из файла input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())

# Измерение времени выполнения
execution_time = timeit.timeit(lambda: last_digit_fib(n), number=1)

# Вывод времени выполнения
print(f"Время выполнения: {execution_time:.6f} секунд")

# Запись результата в файл output.txt
result = last_digit_fib(n)
with open('output.txt', 'w') as file:
    file.write(str(result) + '\n')