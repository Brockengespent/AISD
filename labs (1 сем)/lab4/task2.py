from collections import deque

def process_queue(commands):
    queue = deque()
    results = []

    for command in commands:
        if command.startswith('+'):
            _, number = command.split()
            queue.append(int(number))
        elif command == '-':
            if queue:
                results.append(queue.popleft())

    return results

# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Первая строка содержит количество команд
M = int(lines[0].strip())

# Остальные строки содержат команды
commands = [line.strip() for line in lines[1:M+1]]

# Обработка команд
output = process_queue(commands)

# Запись результатов в файл output.txt
with open('output.txt', 'w') as file:
    for result in output:
        file.write(f"{result}\n")
