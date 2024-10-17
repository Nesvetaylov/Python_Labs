# Шаг 1: Ввод строки
input_string = input("Введите строку: ")

# Шаг 2: Инициализация списков
letters = [] # Хранит уникальные буквы
counts = [] # Счётчик повторений букв

# Шаг 3: Фильтрация строчных английских букв и подсчет повторений
for char in input_string:
    if 'a' <= char <= 'z':
        if char in letters: # Увеличиваем счетчик
            index = letters.index(char)
            counts[index] += 1
        else: # Добавляем букву
            letters.append(char)
            counts.append(1)

# Шаг 4: Сортировка букв и их счетчиков
sorted_letters = sorted(letters)
sorted_counts = [counts[letters.index(letter)] for letter in sorted_letters]

# Шаг 5: Вывод результата
for letter, count in zip(sorted_letters, sorted_counts):
    print(f"{letter}{count}")

# ВВОД: fhb5kbfыshfm

# Фильтрация и подсчет: Проходим по каждому символу в строке. Если символ является строчной буквой:
# Если буква уже есть в letters, находим её индекс и увеличиваем соответствующий счетчик в counts.
# Если буквы нет, добавляем её в letters и устанавливаем счетчик в counts равным 1.
# Сортировка: Сортируем letters, а затем создаем sorted_counts на основе отсортированных букв.
# Вывод: Используем zip для вывода каждой буквы и её количества в нужном формате.
