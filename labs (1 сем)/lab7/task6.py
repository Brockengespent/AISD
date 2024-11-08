import time
import tracemalloc

def lis(sequence):
    n = len(sequence)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    # Найти индекс максимальной длины LIS
    max_length = max(dp)
    index = dp.index(max_length)

    # Восстановление LIS
    lis_sequence = []
    while index != -1:
        lis_sequence.append(sequence[index])
        index = prev[index]

    lis_sequence.reverse()
    return max_length, lis_sequence

def process_input(input_file, output_file):
    with open(input_file, 'r') as infile:
        n = int(infile.readline().strip())
        sequence = list(map(int, infile.readline().strip().split()))

    length, lis_sequence = lis(sequence)

    with open(output_file, 'w') as outfile:
        outfile.write(f"{length}\n")
        outfile.write(" ".join(map(str, lis_sequence)) + "\n")

def main():
    # Начало отслеживания времени и памяти
    start_time = time.perf_counter()
    tracemalloc.start()

    process_input('input.txt', 'output.txt')

    # Подсчет времени и памяти
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time:.9f} секунд")
    print(f"Использование памяти: {current / 10**6:.6f} MB; Пиковое использование: {peak / 10**6:.6f} MB")

if __name__ == "__main__":
    main()
