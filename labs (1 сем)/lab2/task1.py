import time
import tracemalloc

def merge(arr, left, mid, right):
    # Создаем временные массивы
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left

    # Слияние временных массивов обратно в arr
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы L, если есть
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы R, если есть
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Сортируем первую и вторую половины
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Сливаем отсортированные половины
        merge(arr, left, mid, right)

# Начало отслеживания времени и памяти
start_time = time.perf_counter()
tracemalloc.start()

# Чтение из файла input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))

# Сортировка массива
merge_sort(array, 0, n - 1)

# Запись в файл output.txt
with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, array)))

# Подсчет времени и памяти
end_time = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {end_time - start_time:.9f} секунд")
print(f"Использование памяти: {current / 10**6:.6f} MB; Пиковое использование: {peak / 10**6:.6f} MB")
