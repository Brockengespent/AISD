import time
import tracemalloc

def generate_worst_case(n):
    return list(range(n, 0, -1))

def main():
    # Начало отслеживания времени и памяти
    start_time = time.perf_counter()
    tracemalloc.start()

    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())

    # Генерация худшего случая для QuickSort
    worst_case_array = generate_worst_case(n)

    # Запись результата в файл output.txt
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, worst_case_array)))

    # Подсчет времени и памяти
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time:.9f} секунд")
    print(f"Использование памяти: {current / 10**6:.6f} MB; Пиковое использование: {peak / 10**6:.6f} MB")

if __name__ == "__main__":
    main()