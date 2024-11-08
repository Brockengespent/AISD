import timeit

def calc_fib(n):
    if n <= 1:
        return n
    
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

# Чтение числа из файла input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())

# Измерение времени выполнения
execution_time = timeit.timeit(lambda: calc_fib(n), number=1)

# Вывод времени выполнения
print(f"Время выполнения: {execution_time:.6f} секунд")

# Запись результата в файл output.txt
result = calc_fib(n)
with open('output.txt', 'w') as file:
    file.write(str(result) + '\n')
