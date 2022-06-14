# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you want to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""
"""
I am a comment


"""
# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like random and time packages we've discussed about)
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")
game_is_on = True
print("helllooo welcome honey")


# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
while True:
    user_choice = input("choose one of the numbers: rock(1) paper(2) scissors(3)")
    while user_choice != "1" and user_choice != "2" and user_choice != "3":
        print("wrong answer darling, choose again 1 or 2 or 3")
        user_choice = input("choose one of the numbers: rock(1) paper(2) scissors(3)")
    else:
        computer_choice = random.randint(1,3)
        user_choice = int(user_choice)

    #case: user choose rock
    if user_choice == 1 and computer_choice == 3:
        print("yaayyy rock wins scissors, you won")
    elif user_choice == 1 and computer_choice == 2:
        print("damm rock loses to paper, you lost")
    elif user_choice ==1 and computer_choice == 1:
        print("mmm.. rock and rock are equals, its a draw, play again")

    #case: user choose paper
    if user_choice == 2 and computer_choice == 1:
        print("yaayyy paper wins rock, you won")
    elif user_choice == 2 and computer_choice == 3:
        print("damm paper loses to scissors, you lost")
    elif user_choice == 2 and computer_choice == 2:
        print("mmm.. paer equals paper ,its a draw play again")

    #case: user choose scissors
    if user_choice == 3 and computer_choice == 2:
        print("yaayyy scissors wins paper, you won")
    elif user_choice == 3 and computer_choice == 1:
        print("damm scissors loses to rock, you lost")
    elif user_choice == 3 and computer_choice == 3:
        print(" scissors equals scissors, its a draw, play again")

    continue_request = True
    continue_answer = input("wanna continue? y/n").lower()
    while continue_answer != "y" and continue_answer != "n" and continue_request:
        print("eror try again from the option u have been given")
        continue_answer = input("wanna continue? y/n")
    else:
        if continue_answer == "y":
            continue_request = False
        elif continue_answer == "n":
            print("thank u for playing with me see u soon")
            game_is_on = False















    """
      This is the game's heart. You'll need to think and use everything we've learned so far to make this game work.
      Remember Python's rules ( the ':' after a statement, the indentation with loops and statements..)
      
      """
