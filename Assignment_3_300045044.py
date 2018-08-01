##################################################
##  ITI 1120 Intro to Computing Assignment 3     #
##  Hope, Graydon                                #
##  300045044                                    #
##  Professor: Sadiq Abbas                       #
##################################################

from random import shuffle
import random
       
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    shuffle(deck)

def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board


def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')
        

def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print()
    

def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    
    discovered[p1 - 1] = original_board[p1 - 1]
    discovered[p2 - 1] = original_board[p2 - 1]
    print_board(discovered)


def ascii_name_plaque(name):
    ''' (str)->None
    Draws/Prints name plaque'''
    print(5*"*"+len(name)*"*"+5*"*")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print("*  "+2*"_"+name+2*"_"+"  *")
    print("*"+4*" "+len(name)*" "+4*" "+"*")
    print(5*"*"+len(name)*"*"+5*"*")


#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board = []

    for x in l:
        playable_board.append(x)
        if x == '*':
            playable_board.remove(x)

    for index in reversed(playable_board):
        count = playable_board.count(index)
        
        if count % 2 != 0:
            playable_board.remove(index)
        
          
    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''
    for index in l:
        if l.count(index) != 2:
            return
    return True


def alt_deckS(deck):
    '''(list) -> list
    Returns a list of star characters "*" multiplied by the length of the input string (our deck length)
    Precondition: None
    Changes the deck into a hidden form so the user cannot see what numbers/characters are in that location.
    '''
    alt_deck = ['*'] * len(deck)
    return alt_deck

#####################################################################
##  Play Game Section                                               #
#####################################################################

ascii_name_plaque('Welcome to my Concentration game')


def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    num_cards = len(board)
    game = False
    score = 0
    guess_counter = 0
    
    if len(board) < 2:
        for i in range(60):
            print('\n')
        print("Shuffling the deck...")
        print('\n')
        wait_for_player()
        for i in range(60):
            print('\n')
        print("The resulting board is empty.\nPlaying Concentration game with an empty board is impossible.\nGood bye")
        return
    
    for i in range(75):
            print('\n')
    
    print("Ready to play ...\n")
    alternative_deck = alt_deckS(board)
    print_board(alternative_deck)
    print('\n')

##  While the game is False, by our Boolean description, our game will keep prompting the user for valid inputs until they have beat the game.
    
    while game is False:
        print("\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1,6]")
        input_1 = int(input("Enter position 1: "))
        input_2 = int(input("Enter position 2: "))

##  This while loop checks to see if the user is entering valid positions, or locations that have not been entered previously.
        
        while input_1 == input_2 or input_1 not in range(1, num_cards + 1) or input_2 not in range(1, num_cards + 1) or alternative_deck[input_1 -1] != '*' or alternative_deck[input_2 - 1] != '*':
            if input_1 == input_2:
                print("You chose the same position.\nPlease try again.")
                print("\nEnter two distinct positions on the board that you want revealed.\ni.e two integers in the range [1,6]")
            
            elif input_1 not in range(1, num_cards + 1) or input_2 not in range(1, num_cards + 1):
                print("Out of range.\nPlease try again. This guess did not count. Your current number of guesses is " + str(guess_counter))
                

            elif alternative_deck[input_1 -1] != '*' or alternative_deck[input_2 - 1] != '*':
                print("One or both of your chosen positions has already been paired.\nPlease try again. This guess did not count. Your current number of guesses is " + str(guess_counter))
            
            input_1 = int(input("Enter position 1: "))
            input_2 = int(input("Enter position 2: "))            

        print_revealed(alternative_deck, input_1, input_2, board)

        guess_counter = guess_counter + 1

        best_possible_score = num_cards / 2

        final_score = int(guess_counter) - int(best_possible_score)

        wait_for_player()
        for i in range(75):
            print('\n')

        if alternative_deck[input_1 - 1] != board[input_2 - 1]:
            alternative_deck[input_1 -1] = '*'
            alternative_deck[input_2 - 1] = '*'
        else:
            score = score + 1

        if score / num_cards == 0.5:
            game = True

        else:
            print_board(alternative_deck)
            
    print("\nCongratulations! You completed the game with " + str(guess_counter) + " guesses. That is " + str(final_score) + " more than the best possible")

    
##  Main

user_input = input("Would you like (enter 1 or 2 to indicate your choice: \n(1) me to generate a rigorous deck of cards for you \n(2) or, would you like me to read a deck from a file \n")

##  These if and else statements check whether the user is initally entering a proper command (1, 2), as these are our games only available options.
##  It then checks to see if the user is inputting valid (even, in range) card numbers for their generated deck of cards.
##  If these parameters are all met, the game continues into the next part: the Play Game section.

if user_input == '1':
    print("You have chosen to have a rigorous deck generated for you")
    num_cards = int(input("\nHow many cards do you want to play with? \nEnter an even number between 2 and 52: "))
    if (num_cards % 2) == 0 and num_cards <= 52 and num_cards >= 2:
        print("Shuffling the deck...")
        deck = create_board(num_cards)
        shuffle_deck(deck)
        wait_for_player()
        play_game(deck)
                   
    else:
        while (num_cards % 2) != 0 or num_cards > 52 or num_cards < 2:
            num_cards = int(input("\nHow many cards do you want to play with? \nEnter an even number between 2 and 52: "))
            if (num_cards % 2) == 0 and num_cards <= 52 and num_cards >= 2:
                print("Shuffling the deck...")
                deck = create_board(num_cards)
                shuffle_deck(deck)
                wait_for_player()
                play_game(deck)
                   
elif user_input == '2':
    print("You chose to load a deck of cards from a file")
    file=input("Enter the name of the file: ")
    file=file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)

    if is_rigorous(board) == True:
        ascii_name_plaque('This deck is now playable and rigorous and it has ' + str(len(board)) + ' cards')
    else:
        ascii_name_plaque('This deck is now playable but not rigorous and it has ' + str(len(board)) + ' cards')

    wait_for_player()
    for i in range(75):
        print('\n')

    play_game(board)
    
else:
    while user_input != '1' and user_input != '2':
        user_input = input(str(user_input) + " is not an existing option. Please try again. Enter 1 or 2 to indicate your choice \n")
        if user_input == '1':
            print("You have chose to have a rigorous deck generated for you")
            num_cards = int(input("\nHow many cards do you want to play with? \nEnter an even number between 2 and 52: "))
            if (num_cards % 2) == 0 and num_cards <= 52 and num_cards >= 2:
                print("Shuffling the deck...")
                deck = create_board(num_cards)
                shuffle_deck(deck)
                wait_for_player()
                play_game(deck)
                   
            else:
                while (num_cards % 2) != 0 or num_cards > 52 or num_cards < 2:
                    num_cards = int(input("\nHow many cards do you want to play with? \nEnter an even number between 2 and 52: "))
                    if (num_cards % 2) == 0 and num_cards <= 52 and num_cards >=2:
                        print("Shuffling the deck...")
                        deck = create_board(num_cards)
                        shuffle_deck(deck)
                        wait_for_player()
                        play_game(deck)
            
        elif user_input == '2':
            print("You chose to load a deck of cards from a file")
            file=input("Enter the name of the file: ")
            file=file.strip()
            board=read_raw_board(file)
            board=clean_up_board(board)
            
            if is_rigorous(board) == True:
                ascii_name_plaque('This deck is now playable and rigorous and it has ' + str(len(board)) + ' cards')
            else:
                ascii_name_plaque('This deck is now playable but not rigorous and it has ' + str(len(board)) + ' cards')

            wait_for_player()
            for i in range(75):
                print('\n')

            play_game(board)


##  End of Assignment
