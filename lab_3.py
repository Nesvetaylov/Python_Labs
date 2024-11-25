def count_friendly_dominoes(file_input, file_output):
    with open(file_input, 'r') as f:
        N = int(f.readline().strip())
        dominoes = [tuple(sorted(map(int, f.readline().strip().split()))) for _ in range(N)]

    domino_count = {}

    for domino in dominoes:
        if domino in domino_count:
            domino_count[domino] += 1
        else:
            domino_count[domino] = 1

    pairs_count = 0
    used_pairs = set()

    for domino, count in domino_count.items():
        if count > 1 and domino not in used_pairs:
            pairs_count += 1
            used_pairs.add(domino)

    with open(file_output, 'w') as f:
        f.write(str(pairs_count))

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
