"""
Hangman.

Authors: Jiadi Wang and Jingyi Jia(Alan).
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
import random

# DONE: 2. Implement Hangman using your Iterative Enhancement Plan.
def main():
    print("Welcome to Hangman! Hope you can have a great game!")
    one_complete_game()
    while True:
        respond = input('Play another game? (y/n):')
        if respond == 'y':
            one_complete_game()
        if respond == 'n':
            print('Thanks for playing hangman! Have a nice day!')
            break

def one_complete_game():
    guess_count=int(input('How many unsuccessful choices do you want to allow yourself:'))
    word = pick_a_word()
    wordlist = list_of_word(word)
    guess = '-'* len(word)
    guesslist = list_of_word(guess)
    print('The word we choose is:',guess)
    process_of_guess(wordlist,guess_count,guesslist)

def process_of_guess(word,n,guess):
    while True:
        if guess == word:
            newword = tuple_of_word(guess)
            print('Fantastic! You got the word: ', newword, '!')
            break
        letter_entered = input('What letter do you want to try: ')
        if is_in_word(letter_entered,word) == True:
            if guess != word:
                index = index_of_letter_in_the_word(letter_entered,word)
                for j in range(len(index)):
                    guess[index[j]]=letter_entered
                newword = tuple_of_word(guess)
                print('Nice job, you made a successful guess! You still have', n, 'unsuccessful guess before loss the game.')
                print('Here is what you currently know about the secret word: ',newword)
        if is_in_word(letter_entered,word) == False:
            n = n - 1
            print('Sorry bro, here is no',letter_entered,'letter in the word, and you have ', n, 'unsuccessful guess left.')
            if n == 0:
                secretword = tuple_of_word(word)
                print('What a pity! You failed and the secret word was',secretword)
                break

def pick_a_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()
        r = random.randrange(0,len(words))
        item = words[r]
        return item

def index_of_letter_in_the_word(letter,sequence):
    index=[]
    for k in range(len(sequence)):
        if letter == sequence[k]:
            index = index+[k]
    return index

def list_of_word(word):
    wordlist=[]
    for k in range(len(word)):
        wordlist = wordlist + [word[k]]
    return wordlist

def tuple_of_word(word):
    strofword=''
    for k in range(len(word)):
        strofword = strofword + str(word[k])
    return strofword

def is_in_word(letter,sequence):
    for k in range(len(sequence)):
        if letter == sequence[k]:
            return True
    return False




####### Do NOT attempt this assignment before class! #######

main()
