import time
import tracemalloc

def insertion_sort_with_swaps(arr):
    swaps = []
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps.append(f"Swap elements at indices {i + 1} and {min_index + 1}.")
    return swaps

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))

    # Начало отслеживания времени и памяти
    start_time = time.perf_counter()
    tracemalloc.start()

    # Получение списка операций перестановки
    swaps = insertion_sort_with_swaps(array)

    # Окончание отслеживания времени и памяти
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

    # Запись операций в файл output.txt
    with open('output.txt', 'w') as file:
        for swap in swaps:
            file.write(swap + '\n')
        file.write("No more swaps needed.\n")

    # Вывод времени и памяти
    print(f"Время выполнения: {end_time - start_time:.6f} секунд")
    print(f"Использование памяти: {peak / 10**6:.6f} МБ")

if __name__ == "__main__":
    main()
