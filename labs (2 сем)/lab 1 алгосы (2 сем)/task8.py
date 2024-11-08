import time
import psutil
import os

# Запуск таймера
start_time = time.perf_counter()

# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    # Проверка на наличие хотя бы одной строки в файле
    if len(lines) < 1:
        raise ValueError("Файл input.txt должен содержать как минимум одну строку: количество заявок.")
    
    # Чтение количества заявок
    N = int(lines[0].strip())
    
    # Проверка ограничений на N
    if not (1 <= N <= 1000):
        raise ValueError("Количество заявок N должно быть в диапазоне от 1 до 1000.")
    
    # Чтение временных интервалов для каждой заявки
    intervals = []
    for i in range(1, N + 1):
        s, f = map(int, lines[i].strip().split())
        # Проверка ограничений на s и f
        if not (1 <= s < f <= 1440):
            raise ValueError(f"Временные интервалы {s} и {f} выходят за пределы допустимого диапазона (1-1440).")
        intervals.append((s, f))

# Сортировка заявок по времени окончания
intervals.sort(key=lambda x: x[1])

# Выбор непересекающихся заявок
count = 0
last_end_time = 0

for s, f in intervals:
    if s >= last_end_time:
        last_end_time = f
        count += 1

# Запись результата в файл
with open('output.txt', 'w') as file:
    file.write(str(count))

# Остановка таймера и вывод времени выполнения
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.12f} секунд")

# Проверка использования памяти
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss / (1024 * 1024) 
print(f"Использование памяти: {memory_usage:.2f} МБ")

# Проверка ограничения по памяти
if memory_usage > 256:
    raise MemoryError("Использование памяти превысило 256 МБ")
