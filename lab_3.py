def count_friendly_dominoes(file_input, file_output):
    with open(file_input, 'r') as f:
        N = int(f.readline().strip())  # Читаем количество доминошек
        dominoes = [tuple(sorted(map(int, f.readline().strip().split()))) for _ in range(N)]  # Читаем каждую доминошку

    # Используем словарь для подсчета количества каждой доминошки
    domino_count = {}

    for domino in dominoes:
        if domino in domino_count:
            domino_count[domino] += 1
        else:
            domino_count[domino] = 1

    # Подсчитываем количество уникальных пар дружных доминошек
    pairs_count = 0
    used_pairs = set()  # Множество для хранения уже учтенных пар

    for domino, count in domino_count.items():
        if count > 1 and domino not in used_pairs:
            # Если у нас есть больше одной такой доминошки, мы можем выбрать 2 из них
            pairs_count += 1  # Увеличиваем счетчик пар
            used_pairs.add(domino)  # Добавляем пару в множество использованных

    with open(file_output, 'w') as f:
        f.write(str(pairs_count))  # Записываем результат в выходной файл

# Пример использования функции
count_friendly_dominoes('input.txt', 'output.txt')

#Test inputs
# 7
# 1 2
# 2 1
# 3 3
# 4 5
# 2 1
# 6 6
# 6 6
