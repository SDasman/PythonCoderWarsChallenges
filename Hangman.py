import random
words = ['chicken', 'turkey', 'pork', 'tofu',' beef']
word = words[random.randint(0, 4)]
print(word)
letters_guessed = []
correct_letters = []

word_not_guessed = True
while word_not_guessed is True:
    letter = input('Please input a letter to check: ')
    letters_guessed.append(letter)
    letters_set = set(letters_guessed)
    for word in words:
        if letters_set & set(word):
            print('Yes! that letter exists!')
            correct_letters.append(letters_set)

        elif len(word) == len(letters_guessed):
            print('Yes! that letter exists!')
            word_not_guessed = False
            correct_letters.append(letters_set)
        else:
            print('Nada amigo')