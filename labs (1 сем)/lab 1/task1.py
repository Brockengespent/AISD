import time
import tracemalloc

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))

    # Начало отслеживания времени и памяти
    start_time = time.perf_counter()
    tracemalloc.start()

    # Сортировка массива
    insertion_sort(array)

    # Окончание отслеживания времени и памяти
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    # Запись отсортированного массива в файл output.txt
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, array)))

    # Вывод времени и памяти
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использование памяти: {peak / 10**6:.6f} МБ")

if __name__ == "__main__":
    main()
