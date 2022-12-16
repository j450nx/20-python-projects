# have a python dictionary that has a key/value pair that represents the word and its definition
# collect input from the user, input is a word
# check if the word is in the dictionary, then print the definition

def main():
    word_dictionary = {
        'hi': 'a way of greeting',
        'eyes': 'organs for seeing',
        'Earth': 'third rock from the Sun'
    }

    while True:
        word = input('Enter a word (hi/eyes/Earth): ')
        if word == '':
            print('Bye!')
            break
        if word in word_dictionary:
            print(word, ':', word_dictionary[word])

main()