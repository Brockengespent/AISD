import time

def largest_number(numbers):
    from functools import cmp_to_key

    # Функция сравнения для сортировки
    def compare(x, y):
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    # Преобразуем числа в строки
    numbers = list(map(str, numbers))
    
    # Сортируем числа по нашему правилу
    numbers.sort(key=cmp_to_key(compare))
    
    # Объединяем отсортированные числа в одно
    largest_num = ''.join(numbers)
    
    # Убираем ведущие нули (если есть)
    return largest_num.lstrip('0') or '0'   

# Запуск таймера
start_time = time.time()

# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    # Проверка на наличие хотя бы двух строк в файле
    if len(lines) < 2:
        raise ValueError("Файл input.txt должен содержать как минимум две строки: количество чисел и сами числа.")
    
    # Чтение количества чисел
    n = int(lines[0].strip())
    
    # Проверка, что количество чисел больше нуля и не превышает 100
    if n == 0:
        raise ValueError("Количество чисел должно быть больше нуля.")
    if n > 100:
        raise ValueError("Количество чисел не должно превышать 100.")
    
    # Чтение чисел и преобразование их в список целых чисел
    numbers = list(map(int, lines[1].strip().split()))
    
    # Проверка, что количество чисел соответствует указанному значению n
    if len(numbers) != n:
        raise ValueError("Количество чисел не соответствует указанному значению.")
    
    # Проверка, что все числа в диапазоне от 1 до 1000
    for number in numbers:
        if number < 1 or number > 1000:
            raise ValueError(f"Число {number} выходит за пределы допустимого диапазона (1-1000).")

# Получение наибольшего числа
result = largest_number(numbers)

# Запись результата в файл
with open('output.txt', 'w') as file:
    file.write(result)

# Остановка таймера и вывод времени выполнения
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.6f} секунд")