import pandas as pd

# Download word repository
!wget https://raw.githubusercontent.com/dwyl/english-words/master/words.txt

# Read words file
oxford = pd.read_fwf('words.txt', header=None)
oxford = list(oxford[0].str.upper())

# Choose or initialise a word for the game
word = "BLINK"

# Function to check input word against correct word
def check_word(input_word):
    if input_word==word:
        print('hurrah!')
        return True
    else:
        flag = True
        for i,j in zip(range(5),['First', 'Second', 'Third', 'Fourth', 'Fifth']):
            if input_word[i]==word[i]:
                print(j,'block green')
                flag=False
            elif input_word[i] in word:
                print(j,'block yellow')
                flag=False
        if flag:
            print('all blocks gray')
        return False

# Function to start game
def start_game():
    chance = 0
    print('\nYou have 6 tries')
    while chance<6:
        print('Try number', chance+1)
        print('Input your word')
        input_word = input().strip().upper()
        print('Your word is', input_word)
        if len(input_word)==5 and input_word in oxford:
            if check_word(input_word):
                break
            chance+=1
        else:
            print('invalid word, try again')
    if chance==6:
        print('You lost')
        
 start_game()
