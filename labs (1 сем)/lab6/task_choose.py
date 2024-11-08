def calculate_task_numbers(group_number, student_number, group_size, surname):
    # Последние 2 цифры номера группы
    A = int(str(group_number)[-2:])
    
    # Следующее простое число большее, чем количество человек в группе
    def next_prime(n):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        prime = n + 1
        while not is_prime(prime):
            prime += 1
        return prime
    
    p = next_prime(group_size)
    
    # Сумма кодов ASCII всех букв фамилии
    B = sum(ord(char) for char in surname)
    
    # Вычисление номеров задач
    task1 = (A * student_number % p) % 9
    task2 = ((A * student_number + B) % p) % 9
    
    # Проверка на подряд идущие задачи
    if task1 == task2 or task1 + 1 == task2:
        task2 = (task2 + 2) % 9
    
    return task1, task2


group_number = 3239
student_number =20
group_size = 40
surname = "Смирнов"

task1, task2 = calculate_task_numbers(group_number, student_number, group_size, surname)
print(f"Номер первой задачи: {task1}")
print(f"Номер второй задачи: {task2}")