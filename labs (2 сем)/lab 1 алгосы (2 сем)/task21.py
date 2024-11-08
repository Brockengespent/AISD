import time
import psutil
import os

def can_beat_all_cards(player_cards, attack_cards, trump_suit):
    # Разделение карт игрока на козырные и некозырные
    trump_cards = [card for card in player_cards if card[1] == trump_suit]
    non_trump_cards = [card for card in player_cards if card[1] != trump_suit]

    # Функция для проверки, может ли карта b побить карту a
    def can_beat(a, b):
        if a[1] == b[1]:  # Одинаковая масть
            return ranks.index(b[0]) > ranks.index(a[0])
        if b[1] == trump_suit:  # Карта b козырная
            return True
        return False

    # Сортировка карт по рангу
    non_trump_cards.sort(key=lambda x: ranks.index(x[0]))
    trump_cards.sort(key=lambda x: ranks.index(x[0]))

    for attack_card in attack_cards:
        beaten = False
        for card in non_trump_cards:
            if can_beat(attack_card, card):
                non_trump_cards.remove(card)
                beaten = True
                break
        if not beaten:
            for card in trump_cards:
                if can_beat(attack_card, card):
                    trump_cards.remove(card)
                    beaten = True
                    break
        if not beaten:
            return "NO"
    return "YES"

# Запуск таймера
start_time = time.perf_counter()

# Чтение входных данных из файла
with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    # Проверка на наличие хотя бы трех строк в файле
    if len(lines) < 3:
        raise ValueError("Файл input.txt должен содержать как минимум три строки: количество карт у игрока, количество карт для отбивания и козырную масть, карты игрока и карты для отбивания.")
    
    # Чтение количества карт у игрока, количества карт для отбивания и козырной масти
    N, M, R = lines[0].strip().split()
    N, M = int(N), int(M)
    
    # Проверка ограничений на N и M
    if not (1 <= N <= 35):
        raise ValueError("Количество карт у игрока N должно быть в диапазоне от 1 до 35.")
    if not (1 <= M <= 4):
        raise ValueError("Количество карт для отбивания M должно быть в диапазоне от 1 до 4.")
    if not (1 <= M <= N):
        raise ValueError("Количество карт для отбивания M не должно превышать количество карт у игрока N.")
    
    # Чтение карт игрока и карт для отбивания
    player_cards = lines[1].strip().split()
    attack_cards = lines[2].strip().split()
    
    # Проверка, что количество карт у игрока соответствует N
    if len(player_cards) != N:
        raise ValueError("Количество карт у игрока не соответствует указанному значению N.")
    
    # Проверка, что количество карт для отбивания соответствует M
    if len(attack_cards) != M:
        raise ValueError("Количество карт для отбивания не соответствует указанному значению M.")

# Ранги карт в порядке возрастания старшинства
ranks = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# Проверка возможности отбить все карты
result = can_beat_all_cards(player_cards, attack_cards, R)

# Запись результата в файл
with open('output.txt', 'w') as file:
    file.write(result)

# Остановка таймера и вывод времени выполнения
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.12f} секунд")

# Проверка использования памяти
process = psutil.Process(os.getpid())
memory_usage = process.memory_info().rss / (1024 * 1024)  # Преобразование в мегабайты
print(f"Использование памяти: {memory_usage:.2f} МБ")

# Проверка ограничения по памяти
if memory_usage > 16:
    raise MemoryError("Использование памяти превысило 16 МБ")
