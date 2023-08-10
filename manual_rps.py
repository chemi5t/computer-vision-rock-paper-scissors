import random

def get_computer_choice(): # randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
    action_list = ["Rock", "Paper", "Scissors"] # create 'action_list' of hand gesture selections
    action = random.choice(action_list)
    return action

def get_user_choice(): # User to enter a choice
    while True:
      action_list = ["Rock", "Paper", "Scissors"] # create 'action_list' of hand gesture selections
      choice = input("Please enter a choice: ").capitalize()  # Convert guess to lowercase
      if choice in action_list: # Check guess is valid from list assigned
         return choice
      else:
         print("Oops! That is not a valid input. Choose from 'rock, 'paper' or scissors.")

# def get_winner(computer_choice, user_choice):
#        if computer_choice == "rock" and user_choice == "paper":
#           return "You won! User's paper beats rock."
#        elif computer_choice == "rock" and user_choice == "scissors":
#           return "You lost. Computer's rock beats sissors."
#        elif computer_choice == "rock" and user_choice == "rock":
#           return "It is a tie!"
#        elif computer_choice == "paper" and user_choice == "scissors":
#           return "You won! User's scissors beat paper."
#        elif computer_choice == "paper" and user_choice == "rock":
#           return "You lost. Computer's paper beats rock."
#        elif computer_choice == "paper" and user_choice == "paper":
#           return "It is a tie!"
#        elif computer_choice == "scissors" and user_choice == "rock":
#           return "You won! User's rock beats scissors."
#        elif computer_choice == "scissors" and user_choice == "paper":
#           return "You lost. Computer's scissors beat paper."
#        else:
#           return "It is a tie!"

def get_winner(computer_choice, user_choice):
    if computer_choice == "Rock" and user_choice == "Paper":
        return "You won! User's Paper beats Rock."
    elif computer_choice == "Rock" and user_choice == "Scissors":
        return "You lost. Computer's Rock beats Scissors."
    elif computer_choice == "Rock" and user_choice == "Rock":
        return "It is a tie!"
    elif computer_choice == "Paper" and user_choice == "Scissors":
        return "You won! User's Scissors beat Paper."
    elif computer_choice == "Paper" and user_choice == "Rock":
        return "You lost. Computer's Paper beats Rock."
    elif computer_choice == "Paper" and user_choice == "Paper":
        return "It is a tie!"
    elif computer_choice == "Scissors" and user_choice == "Rock":
        return "You won! User's Rock beats Scissors."
    elif computer_choice == "Scissors" and user_choice == "Paper":
        return "You lost. Computer's Scissors beat Paper."
    else:
        return "It is a tie!"

def play():
    action = get_computer_choice()
    choice = get_user_choice()
    print(f"Computer's choice: {action}")
    result = get_winner(action, choice)
    print(result)

if __name__ == "__main__":
    play()
