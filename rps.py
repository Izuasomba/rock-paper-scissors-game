from random import*
c = ["rock","paper","scissors"]
user = 0
computer = choice(c)
d=0
def user_input():
    global user
    user = input("please type rock, paper or scissors: ").lower()
    return user
def computer_choice():
    global c
    global computer
    return computer
def result():
    global user
    global c
    global computer
    while user not in c:
        user_input()      
    if user == computer:
        print(f"You chose {user}, and computer chose {computer}")
        print("It's a tie")
    if user == "rock" and computer == "paper":
        print(f"You chose {user}, and computer chose {computer}")
        print ("Computer wins")
    elif user == "paper" and computer == "rock":
        print(f"You chose {user}, and computer chose {computer}")
        print("You win")
    if user == "rock" and computer == "scissors":
        print(f"You chose {user}, and computer chose {computer}")
        print("you win")
    elif user == "scissors" and computer == "rock":
        print(f"You chose {user}, and computer chose {computer}")
        print("computer wins")
    if user == "scissors" and computer == "paper":
        print(f"You chose {user}, and computer chose {computer}")
        print("You win")
    elif user == "paper" and computer == "scissors":
        print(f"You chose {user}, and computer chose {computer}")
        print("Computer wins")
    return user

def play_game():
    user_input()
    result()

def play_again():
   global d
   d=input("Play again? y/n: ")
   while d=="y":
    play_game()
    while d == "n":
        print("see you soon")
        break
    return d

def start():
    play_game()
    play_again()
    return play_again()
   
start()
play_again()
   

    

        