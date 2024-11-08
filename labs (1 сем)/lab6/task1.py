import time
import tracemalloc

def process_operations():
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        n = int(infile.readline().strip())
        my_set = set()
        
        for _ in range(n):
            operation = infile.readline().strip().split()
            op_type = operation[0]
            if op_type == 'A':
                x = int(operation[1])
                my_set.add(x)
            elif op_type == 'D':
                x = int(operation[1])
                my_set.discard(x)
            elif op_type == '?':
                x = int(operation[1])
                if x in my_set:
                    outfile.write('Y\n')
                else:
                    outfile.write('N\n')

def main():
    # Начало отслеживания времени и памяти
    start_time = time.perf_counter()
    tracemalloc.start()

    # Обработка операций
    process_operations()

    # Подсчет времени и памяти
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Время выполнения: {end_time - start_time:.9f} секунд")
    print(f"Использование памяти: {current / 10**6:.6f} MB; Пиковое использование: {peak / 10**6:.6f} MB")

if __name__ == "__main__":
    main()
