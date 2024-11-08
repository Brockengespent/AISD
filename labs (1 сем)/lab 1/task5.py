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

    # Сортировка массива
    insertion_sort(array)

    # Запись отсортированного массива в файл output.txt
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, array)))

if __name__ == "__main__":
    main()
