def check_brackets(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    opening_brackets = set(bracket_map.values())

    for i, char in enumerate(s):
        if char in opening_brackets:
            stack.append((char, i + 1))
        elif char in bracket_map:
            if stack and stack[-1][0] == bracket_map[char]:
                stack.pop()
            else:
                return i + 1

    if stack:
        return stack[0][1]

    return "Success"

# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    s = file.readline().strip()

# Проверка скобочной последовательности
result = check_brackets(s)

# Запись результата в файл output.txt
with open('output.txt', 'w') as file:
    file.write(f"{result}\n")
