import random

def get_computer_choice(): # randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
    action_list = ["rock", "paper", "scissors"] # create 'action_list' of hand gesture selections
    action = random.choice(action_list)
    return action

def get_user_choice(): # User to enter a choice
    while True:
      action_list = ["rock", "paper", "scissors"] # create 'action_list' of hand gesture selections
      choice = input("Please enter a choice: ").lower()  # Convert guess to lowercase
      if choice in action_list: # Check guess is valid from list assigned
         return choice
      else:
         print("Oops! That is not a valid input. Choose from 'rock, 'paper' or scissors.")

def get_winner(computer_choice, user_choice):
       if computer_choice == "rock" and user_choice == "paper":
          return "You won! User's paper beats rock."
       elif computer_choice == "rock" and user_choice == "scissors":
          return "You lost. Computer's rock beats sissors."
       elif computer_choice == "rock" and user_choice == "rock":
          return "It's a tie!"
       elif computer_choice == "paper" and user_choice == "scissors":
          return "You won! User's scissors beat paper."
       elif computer_choice == "paper" and user_choice == "rock":
          return "You lost. Computer's paper beats rock."
       elif computer_choice == "paper" and user_choice == "paper":
          return "It's a tie!"
       elif computer_choice == "scissors" and user_choice == "rock":
          return "You won! User's rock beats scissors."
       elif computer_choice == "scissors" and user_choice == "paper":
          return "You lost. Computer's scissors beat paper."
       else:
          return "It's a tie!"

def play():
    action = get_computer_choice()
    choice = get_user_choice()
    print(f"Computer's choice: {action}")
    result = get_winner(action, choice)
    print(result)

if __name__ == "__main__":
    play()
