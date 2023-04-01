import random

words = ['apple', 'banana', 'cherry', 'orange', 'pineapple', 'grapefruit']
def get_word():
    word = random.choice(words)
    return word

def play(word):
    guessed = ['_'] * len(word)
    letters = []
    mistakes = 0
    while True:
        print(' '.join(guessed))
        guess = input('Guess a letter: ')
        if guess in letters:
            print('You already guessed that letter.')
        elif guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            mistakes += 1
            print('That letter is not in the word.')

        letters.append(guess)
        if ''.join(guessed) == word:
            print('Congratulations, you guessed the word!')
            break
        elif mistakes == 7:
            print('Sorry, you ran out of guesses. The word was', word)
            break
while True:
    word = get_word()
    play(word)
    again = input('Do you want to play again? (y/n): ')
    if again != 'y':
        break
