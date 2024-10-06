letter_count = {}
for char in "fhb5kbfыshfm":
    if 'a' <= char <= 'z':
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

sorted_letters = sorted(letter_count.keys())

for letter in sorted_letters:
    print(f"{letter}{letter_count[letter]}")

'''
1. letter_count = {} Создает пустой словарь letter_count, который будет использоваться для хранения количества каждого строчного английского символа.

2. for char in "fhb5kbfыshfm": Начинает цикл for, который будет перебирать каждый символ в строке "fhb5kbfыshfm".

3. if 'a' <= char <= 'z': Проверяет, является ли текущий символ char строчным английским символом (т.е., между 'a' и 'z' включительно). Если это так, то код внутри условия if будет выполнен.

4. if char in letter_count: Проверяет, есть ли текущий символ char уже в словаре letter_count. Если это так, то код внутри условия if будет выполнен.

5. letter_count[char] += 1 Если символ уже есть в словаре, увеличивает его счетчик на 1.

6. else: letter_count[char] = 1 Если символа нет в словаре, добавляет его в словарь с счетчиком 1.

7. sorted_letters = sorted(letter_count.keys()) Сортирует ключи словаря letter_count (т.е., строчные английские символы) в алфавитном порядке и хранит их в списке sorted_letters.

8. for letter in sorted_letters: Начинает цикл for, который будет перебирать каждый символ в списке sorted_letters.

9. print(f"{letter}{letter_count[letter]}") Выводит символ и его счетчик, разделенные пробелом. Используется форматирование строки с помощью f для создания вывода.
'''
