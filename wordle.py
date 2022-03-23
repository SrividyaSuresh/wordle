import pandas as pd
import wget
import random
import os

# Download word repository
if os.path.exists('words.txt'):
    words_repo = os.path.basename('words.txt')
else:
    words_repo = wget.download('https://raw.githubusercontent.com/dwyl/english-words/master/words.txt')

# Read words file
oxford = pd.read_fwf(words_repo, header=None)
oxford = list(oxford[0].str.upper())

# Choose or initialise a word for the game
word = random.choice(oxford)

# Function to check input word against correct word
def check_word(input_word):
    if input_word==word:
        print('hurrah!')
        return True
    else:
        flag = True
        for i,j in zip(range(5),['First', 'Second', 'Third', 'Fourth', 'Fifth']):
            if input_word[i]==word[i]:
                print(j,'block green,',input_word[i])
                flag=False
            elif input_word[i] in word:
                print(j,'block yellow,',input_word[i])
                flag=False
        if flag:
            print('all blocks gray')
        return False

# Function to start game
def start_game():
    chance = 0
    print('\nYou have 6 tries')
    print(f"\nIt's a {len(word)} letter word")
    while chance<6:
        print('Try number', chance+1)
        print('Input your word')
        input_word = input().strip().upper()
        print('Your word is', input_word)
        if len(input_word) and input_word in oxford:
            if check_word(input_word):
                break
            chance+=1
        else:
            print('invalid word, try again')
    if chance==6:
        print('You lost')
        print(f'The word was << {word} >>')

if __name__ == "__main__":
    start_game()
