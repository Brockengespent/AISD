def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    while True:
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
            left = 2 * i + 1
            right = 2 * i + 2
        else:
            break

def heap_sort(arr):
    n = len(arr)

    # Построение максимальной кучи
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Перемещение текущего корня в конец
        max_heapify(arr, i, 0)

    # Инвертирование массива для убывающего порядка
    arr.reverse()

# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))

# Сортировка массива
heap_sort(arr)

# Запись отсортированного массива в файл output.txt
with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, arr)) + '\n')
