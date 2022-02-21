my_text = '''Послушайте!

Послушайте!
Ведь, если звезды зажигают —
значит — это кому-нибудь нужно?
Значит — кто-то хочет, чтобы они были?
Значит — кто-то называет эти плево́чки жемчужиной?

Владимир Маяковский'''.lower()

print(my_text)

poem_list = my_text.split()

# Найдите и напечатайте список уникальных слов
unique_words = list(set(poem_list))
print(unique_words)

# Найдите сколько раз встречается в нем каждое уникальное слово и напечатайте
word_count = dict((i, poem_list.count(i)) for i in poem_list)
print(word_count)


# Найдите какое слово (слова) используются максимальное количество раз. Напечатайте это слово/слова и сколько раз оно
# встретилось-------------------------------------------------------------------

def most_frequent():
    counter = 0
    frequent = []

    for i in poem_list:
        curr_frequency = poem_list.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            frequent = i

    print(frequent)


most_frequent()

# Найдите и напечатайте среднюю длину уникального слова
total = 0
for i in poem_list:
    total += len(i)
average = total // len(poem_list)
print(average)

# Найдите и напечатайте общее количество слов в тексте
print(len(poem_list))