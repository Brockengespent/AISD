import time
import tracemalloc

def find_majority_element(arr):
    def majority_element_rec(start, end):
        if start == end:
            return arr[start]

        mid = (end - start) // 2 + start
        left = majority_element_rec(start, mid)
        right = majority_element_rec(mid + 1, end)

        if left == right:
            return left

        left_count = sum(1 for i in range(start, end + 1) if arr[i] == left)
        right_count = sum(1 for i in range(start, end + 1) if arr[i] == right)

        return left if left_count > right_count else right

    candidate = majority_element_rec(0, len(arr) - 1)
    count = sum(1 for x in arr if x == candidate)

    return candidate if count > len(arr) // 2 else None

def main():
    # Начало отслеживания времени и памяти
    start_time = time.perf_counter()
    tracemalloc.start()

    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))

    # Поиск элемента большинства
    majority_element = find_majority_element(array)

    # Запись результата в файл output.txt
    with open('output.txt', 'w') as file:
        file.write('1' if majority_element is not None else '0')

    # Подсчет времени и памяти
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time:.9f} секунд")
    print(f"Использование памяти: {current / 10**6:.6f} MB; Пиковое использование: {peak / 10**6:.6f} MB")

if __name__ == "__main__":
    main()