def evaluate_postfix(expression):
    stack = []
    
    for token in expression:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    
    return stack[0]

# Чтение данных из файла input.txt
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    expression = file.readline().strip().split()

# Вычисление значения выражения
result = evaluate_postfix(expression)

# Запись результата в файл output.txt
with open('output.txt', 'w') as file:
    file.write(f"{result}\n")