import time

# Запуск таймера
start_time = time.time()

# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    # Проверка на наличие хотя бы двух строк в файле
    if len(lines) < 2:
        raise ValueError("Файл input.txt должен содержать как минимум две строки: количество минут и количество сапог, а также время починки каждого сапога.")
    
    # Чтение количества минут и количества сапог
    K, n = map(int, lines[0].strip().split())
    
    # Проверка ограничений на K и n
    if not (1 <= K <= 1000):
        raise ValueError("Количество минут K должно быть в диапазоне от 1 до 1000.")
    if not (1 <= n <= 500):
        raise ValueError("Количество сапог n должно быть в диапазоне от 1 до 500.")
    
    # Чтение времени починки каждого сапога
    times = list(map(int, lines[1].strip().split()))
    
    # Проверка, что количество времени починки соответствует количеству сапог
    if len(times) != n:
        raise ValueError("Количество времени починки не соответствует количеству сапог.")
    
    # Проверка ограничений на время починки каждого сапога
    for t in times:
        if not (1 <= t <= 100):
            raise ValueError(f"Время починки {t} выходит за пределы допустимого диапазона (1-100).")

# Сортировка времени починки в порядке возрастания
times.sort()

# Подсчет максимального количества сапог, которые можно починить
total_time = 0
count = 0

for t in times:
    if total_time + t <= K:
        total_time += t
        count += 1
    else:
        break

# Запись результата в файл
with open('output.txt', 'w') as file:
    file.write(str(count))

# Остановка таймера и вывод времени выполнения
end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.6f} секунд")
