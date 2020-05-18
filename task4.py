# 1. Написать функцию (F): на входе указать список имен и целое число N; на выходе - список длины N случайных имен из первого списка$
from random import choices

def F(names, N):
    return choices(names, k=N)
list_names = F(['Nina', 'Anna', 'Ivan', 'Vlad', 'Elena', 'Andrey', 'Nataly', 'Irina', 'Evgeniy', 'Timur', 'Igor', 'Fedor', 'Nicolay', 'Nataly', 'German', 'Sergey', 'Nataly', 'Alex', 'Alena', 'Ksu'], N=100)
print(list_names)

# 2. Напиcать функцию вывода самого частого имени из списка на выходе функции F;
def most_offer(names):
    word = {}
    for name in names:
        word[name] = word.get(name, 0) + 1
    word = list(word.items())
    word.sort(key=lambda x: x[1], reverse=True)
    return word[0][0]
print('Наиболее часто встречаемое имя -', most_offer(list_names))

# 3. Написать функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
def rare_letter(names):
    letters = {}
    for name in names:
        for char in name:
            letters[char] = letters.get(char, 0) + 1
    letters = sorted(list(letters.items()), key=lambda x: x[1])
    return letters[0][0]
print('Самая редкая буква, с которой начинается имя -', rare_letter(list_names))