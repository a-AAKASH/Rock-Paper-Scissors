import random 

def get_computer_choice():
    list = ["Rock", "Paper", "Scissors"]
    chosen_item = random.choice(list)
    return chosen_item

def get_user_choice():
    user_choice = input("Pick one! \n Rock, Paper or Scissors? \n")
    return user_choice.title()

def get_winner(user_choice, computer_choice):
    if user_choice==computer_choice:
        return 0
    elif user_choice=="Rock":
        if computer_choice=="Paper":
            return 1
        elif computer_choice=="Scissors":
            return 2
        else:
            print("Error!")
    elif user_choice=="Paper":
        if computer_choice=="Rock":
            return 2
        elif computer_choice=="Scissors":
            return 1
        else:
            print("Error!")
    elif user_choice=="Scissors":
        if computer_choice=="Rock":
            return 1
        elif computer_choice=="Paper":
            return 2
        else:
            print("Error!")
    else:
        print("User choice not valid. Try again!")
        return 3
        
def play():
    print("Let's play Rock, Paper and Scissors! \n")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("Computer chose: ",computer_choice,"\n")
    get_winner_return_key = get_winner(user_choice, computer_choice)
    if get_winner_return_key==0:
        print("It is a tie!\n Let's play again! \n (Press Ctrl + z if you want to exit!)\n")
        play()
    elif get_winner_return_key==1:
        print("You won")
    elif get_winner_return_key==2:
        print("You lost")
    elif get_winner_return_key==3:
        play_gain = input("Press 1 and Enter to play again \n")
        if play_gain=="1":
            play()
        else:
            print("Thank you for playing! :) ")
    else:
        print("Error!")

play()