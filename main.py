import string

import random_words
from visual import lives_dict

# Welcome console message
print("WELCOME TO THE HANGMAN GAME")


def hangman():
    new_random = random_words.RandomWords()
    word = new_random.random_word().upper()
    print(word)
    word_letters = set(word)  # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user guessed
    chance = 6
    # getting a user input
    while len(word_letters) > 0 and chance >= 0:
        # letter used
        print('You have used these letters: ', ''.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in
                     word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print(lives_dict.get(chance))
                chance -= 1
        elif user_letter in used_letters:
            print("You've already used this character!")
        else:
            print("Invalid character. Please try again.")

    if len(word_letters) <= 0:
        print("CONGRATULATION!")
        print("YOU'VE WON!")
    else:
        print("GAME OVER!")
        print("TRY AGAIN!")


hangman()
