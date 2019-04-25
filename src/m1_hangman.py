"""
Hangman.

Authors: Jonah Egertson and Jared Brown.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import math as m
import random as rand

word = ''

with open('words.txt') as f:
    f.readline()
    string = f.read()
    words = string.split()



def main():
    while True:
        print()
        flag=0
        guesses = int(input('How many wrong guesses do you want allowed? '))
        min_word = int(input('What minimum length do you want for your word? '))
        word = rand_word(min_word)
        words = ['-'] + ['-']*(len(word)-1)
        #print(make_string(hidden_word),word)
        (win_c,lose_c) = game(word,words,guesses)
        if win_c:
            win_condition(word)
        elif lose_c:
            lose_condition(word)
        if restart() == False:
            break
    print()
    print('Thanks for playing! Try again sometime!')


    #print(guess2,make_string(words))



def rand_word(min):
    while True:
        r = rand.randrange(0,len(words))
        if len(words[r]) >= min:
            break
    return words[r]



def make_string(seq):
    string = ''
    for k in range(len(seq)):
        string = string + seq[k]
    return string



def game(word,mod_word,guesses_left):
    lose_c=False
    win_c=False
    prior_guesses = []
    while True:
        (guess2, words, theguess) = guess(word, mod_word)
        prior_guesses = prior_guesses + [theguess]
        if guess2 == True:
            print('Correct!')
            print()
            flag = 0
            for k in range(len(words)):
                if words[k] == '-':
                    flag = 1
            if flag == 0:
                win_c=True
                break
        else:
            guesses_left = guesses_left - 1
            print('Incorrect! Guesses Left:', guesses_left)
            print()
        if guesses_left == 0:
            lose_c = True
            break
        print('Your guesses have been:', prior_guesses)
        print()
    return (win_c,lose_c)



def guess(actual,hidden):
    guess1 = input('The word is: ' + make_string(hidden) + ' ')
    flag = 0
    for k in range(len(actual)):
        if actual[k] == guess1:
            hidden[k] = guess1
            flag = 1
    if flag == 1:
        return (True,hidden,guess1)
    else:
        return (False,hidden,guess1)



def win_condition(actual):
    print('Congratulations!! The word was:',actual)



def lose_condition(actual):
    print('Too bad!! The word was:', actual)


def restart():
    while True:
        check=input('Would you like to play again (y/n)?')
        if check == 'y':
            return True
        elif check == 'n':
            return False
        else:
            print("No, no! y or n! It's not that hard!")
            print('')

main()