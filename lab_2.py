# Ввод данных
num_states = int(input("Введите количество штатов: "))
# Словарь для хранения количества выборщиков по штатам
electors = {}
# Словарь для хранения голосов по кандидатам в каждом штате.
votes = {}

# Считываем информацию о штатах и количестве выборщиков
for _ in range(num_states):
    state_info = input().strip().split()
    state_name = state_info[0]
    elector_count = int(state_info[1])
    electors[state_name] = elector_count
    votes[state_name] = {}

# Ввод количества голосов
num_votes = int(input("Введите количество голосов: "))

# Считываем результаты голосования
for _ in range(num_votes):
    vote_info = input().strip().split()
    state_name = vote_info[0]
    candidate_name = vote_info[1]
    
    if candidate_name not in votes[state_name]:
        votes[state_name][candidate_name] = 0
    votes[state_name][candidate_name] += 1

# Подсчет голосов для каждого кандидата
total_votes = {}
for state, candidates in votes.items():
    # Находим кандидата с наибольшим количеством голосов в штате
    max_votes = max(candidates.values())
    winners = [candidate for candidate, count in candidates.items() if count == max_votes]
    # Наименьший в лексикографическом порядке кандидат
    winner = min(winners)
    
    # Добавляем выборщиков к победителю
    if winner not in total_votes:
        total_votes[winner] = 0
    total_votes[winner] += electors[state]

# Сортировка кандидатов по количеству голосов и имени
sorted_candidates = sorted(total_votes.items(), key=lambda x: (-x[1], x[0]))

# Вывод результата
for candidate, votes in sorted_candidates:
    print(f"{candidate} {votes}")

# Пример ввода:
    # Кол-во штатов: 3
    # Штат1 5
    # Штат2 3
    # Штат3 4
    # Кол-во голосов: 10
    # Штат1 КандидатА
    # Штат1 КандидатБ
    # Штат1 КандидатА
    # Штат2 КандидатБ
    # Штат2 КандидатБ
    # Штат3 КандидатА
    # Штат3 КандидатА
    # Штат3 КандидатБ
    # Штат3 КандидатБ
    # Штат3 КандидатБ