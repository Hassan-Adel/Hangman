#Name: Hassan Mohammad Adel
#ID: 20120154
#Group: CS_IS_2

from random import randint
import time

words = []

with open('wordsList.txt') as f:
    words = f.readlines()

listSize = len(words)

for x in range(0, listSize):
    words[x] = words[x].rstrip('\n')
    words[x] = words[x].lower()
    #print("word", words[x])
        
#print(listSize)

def randomWord():
    randomIndex = randint(0, listSize-1)
    guessedWord = words[randomIndex]
    return guessedWord

def makeDashes(guessedWord):
    dashedWord = []
    for x in guessedWord:
        if(x != ' '):
            dashedWord.append('_')
        else:
            dashedWord.append('-')
    return dashedWord

def displayWord(dashedWord):
    for x in range(0, len(dashedWord)):
        print(dashedWord[x]),
    print(' ')

def isDashed(word):
    for x in range(0, len(word)):
        if(word[x] == '_'):
            return True
    return False


def main():
    
    play = 'true'
    print('WELCOME TO HANGMAN GAME!\n')
    print('Hangman is a popular game where you must ')
    print('guess a randomly selected word to win, guessing just one letter at a time!')
    print('\nHow to play:\n')
    print('- You guess one letter at a time (no digits/word)\n')
    print('- If you guess all the right letters in the word, you win!\n')
    print('- If you make 6 wrong guesses, you lose!\n')
    print('ready?...\n')
    time.sleep(3)
    
    while(play == 'true'):
        chances = 6
        word = randomWord()
        #print(word)
        dashedWord = makeDashes(word)
        triedLetters = []

        displayWord(dashedWord)
        
        while(chances > 0 and isDashed(dashedWord) == True):
            
            letter = raw_input('\nYour guess (letters only): ')
            letter = letter.lower()
            if len(letter) > 1 or not letter.isalpha():
                time.sleep(0.5)
                print('Input must only be a single letter!')
                continue
            
            if letter not in word:
                if letter not in triedLetters:
                    triedLetters.append(letter)
                    time.sleep(0.5)
                    print('The word does not contain this letter!')
                    chances -= 1
                else:
                    time.sleep(0.5)
                    print('You have already tried this letter!')
                    continue
            else:
                if letter in dashedWord:
                    time.sleep(0.5)
                    print('You have already tried this letter!')
                    continue
                else:
                    for x in range(0, len(word)):
                        if(letter == word[x]):
                            dashedWord[x] = letter

            time.sleep(0.5)
            print('Chances Remaining: '  + str(chances))
            time.sleep(0.5)
            print('Missed letters: '),
            for x in triedLetters:
                print(x),
            print('\n')
            time.sleep(0.5)
            displayWord(dashedWord)
            print('\n')

        if(chances > 0):
            print('You Won!\n')
        else:
            print('Game Over!\n')
            print('The word is: ' + word)

        print('\n#####################################################################')
            
        print('\nWould you like to play again?')
        newGame = raw_input('Press Y for Yes or any other key to Quit: ')
        if(newGame != 'y'):
            play = 'false'

main()

