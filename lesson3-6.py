def int_func(user_word):
    new = str()

    for i in user_word:
        if ord(i) < 97 or ord(i) > 122:
            print('Неправильно, исправьте ')
            break

        else:
            new += i
    return new.title()


many_words = input('Введите через пробел строку из слов разделенных пробелами: ').split()
new_words = []
for n in many_words:
    new_words.append(int_func(n))
new_words = ' '.join(new_words)


print(many_words)

