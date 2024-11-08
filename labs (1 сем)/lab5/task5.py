import heapq

def process_tasks(n, tasks):
    # Очередь с приоритетом для потоков (время завершения, индекс потока)
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    
    results = []

    for task_time in tasks:
        # Извлекаем поток с наименьшим временем завершения
        finish_time, thread_index = heapq.heappop(threads)
        # Записываем результат: индекс потока и время начала задачи
        results.append((thread_index, finish_time))
        # Обновляем время завершения для потока и возвращаем в очередь
        heapq.heappush(threads, (finish_time + task_time, thread_index))

    return results

# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    tasks = list(map(int, file.readline().strip().split()))

# Обработка задач
output = process_tasks(n, tasks)

# Запись результатов в файл output.txt
with open('output.txt', 'w') as file:
    for thread_index, start_time in output:
        file.write(f"{thread_index} {start_time}\n")
