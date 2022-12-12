def replace_word():
    str = 'Hello from Mount Albert ON Canada'
    str_arr = str.split(' ')
    print(str)

    while True:
        try:
            word_to_replace = input('Enter the word to replace: ')
        except ValueError:
            continue
        if word_to_replace not in str_arr:
            print('Select a word from the sentence!\n')
            print(str)
        else:
            break

    word_replacement = input('Enter the new word: ')
    print(str.replace(word_to_replace, word_replacement))

replace_word()