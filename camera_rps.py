import cv2
import numpy as np
import random
import time
from keras.models import load_model


class RPS():
    def __init__(self):
        pass
    
    def get_camera_picture_of_user_action(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        countdown_duration = 5  # Countdown 3 seconds before capturing user's actionseconds
        start_time = time.time()
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            self.prediction = model.predict(data)
            elapsed_time = time.time() - start_time
            remaining_time = countdown_duration - elapsed_time
            if remaining_time <= 0:
                break
            print(f"Countdown: {int(remaining_time)} seconds")
            cv2.imshow('frame', frame)
            print(self.prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to close the window
                break
        cap.release() # After the loop release the cap object
        cv2.destroyAllWindows() # Destroy all the windows
        return self.prediction       
    
    def get_prediction(self):
        index_of_user_choice = np.argmax(self.prediction[0])  # Find the index of the maximum predicted value 
        user_action_list = ["Nothing", "Rock", "Paper", "Scissors"]
        self.user_choice = user_action_list[index_of_user_choice]
        return self.user_choice

    def get_computer_choice(self): # randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
        computer_action_list = ["Rock", "Paper", "Scissors"]
        self.computer_choice = random.choice(computer_action_list)
        return self.computer_choice

    def get_winner(self): # Checks computers choice vs users and declare a winner
        if self.computer_choice == "Rock" and self.user_choice == "Paper" or self.computer_choice == "Paper" and self.user_choice == "Scissors" or self.computer_choice == "Scissors" and self.user_choice == "Rock":
            return "You won!"
        elif self.computer_choice == self.user_choice:
            return "It is a tie!"
        else:
            return "You lost."

def play(wins_needed): # Pulls the functions together and plays the RPS game
    computer_wins = 0 
    user_wins = 0
    game = RPS()
    while user_wins < wins_needed and computer_wins < wins_needed:
        computer_choice = game.get_computer_choice()  # Get the computer's choice for each round
        game.get_camera_picture_of_user_action()
        user_choice = game.get_prediction()
        
        print(f"User's choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        result = game.get_winner()
        print(result)
        
        if "You won!" in result:
            user_wins += 1
        elif "You lost." in result:
            computer_wins += 1
        else:
            pass
        
        print(f"User Wins: {user_wins}, Computer Wins: {computer_wins}")

    if user_wins >= wins_needed:
        print("Congratulations! You won the game.")
    else:
        print("Computer wins the game. Better luck next time.")


if __name__ == "__main__":
    wins_needed = int(input("Enter the number of wins needed to end the game: "))
    play(wins_needed)