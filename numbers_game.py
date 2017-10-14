import random

def game():
    def comp_guess(a, b):
        return random.randint(a, b)
    a = 1
    b = 30
    tries = 5
    guesses = []
    try:
        secret_num = int(input("Pick a number between {} and {} for the computer to guess. ".format(a, b)))
    except ValueError:
        print("{} isn't a number.".format(secret_num))
        if ValueError:
            game()
    else:    
        while len(guesses) < tries: # computer has 5 guesses
            random_num = comp_guess(a, b)   #computer generates a random number based on a/b parameters
            if random_num == secret_num:                                    
                print("The computer guessed {}, and was correct!".format(random_num))
                break            
            else:
                more_less = input("The computer guessed {}. Is your number 'HIGHER' or 'LOWER'? ".format(random_num))
                if more_less.lower() == 'higher':
                    a = random_num + 1
                elif more_less.lower() == 'lower':
                    b = random_num - 1
            guesses.append(random_num)          
        else:
            print("The computer was unable to guess the number {} within {} tries. Too bad!".format(secret_num, tries))
        play_again = input("Do you want to play again? Y/n ")
        if play_again.lower() != 'n':
            game()
        else:
            print("Bye!")
game()
