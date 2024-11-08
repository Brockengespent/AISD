def max_subarray(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())
        array = list(map(int, file.readline().strip().split()))

    # Поиск максимального подмассива
    result = max_subarray(array)

    # Запись результата в файл output.txt
    with open('output.txt', 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    main()

