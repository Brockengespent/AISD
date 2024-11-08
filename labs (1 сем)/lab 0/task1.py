# Чтение данных из файла
with open('input.txt', 'r') as file:
    a, b = map(int, file.readline().split())

# Вычисление суммы
result_sum = a + b

# Запись результата суммы в файл
with open('output.txt', 'w') as file:
    file.write(str(result_sum) + '\n')

# Вычисление выражения
result_expression = a + b**2

# Запись результата выражения в файл
with open('output.txt', 'a') as file:
    file.write(str(result_expression) + '\n')