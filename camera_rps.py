import cv2 # Wrapper for the OpenCV (Open Source Computer Vision Library) library.
import numpy as np # NumPy library in Python provides support for multi-dimensional arrays; ndarrays.
import random # random module for generating random numbers and performing various random operations. 
import time # time module in Python provides various functions related to time.
from keras.models import load_model # Imports trained .h5 model.


class RPS():
    """
    Rock-Paper-Scissors (RPS) Game Class.
    
    This class provides a simple implementation of the Rock-Paper-Scissors game using a webcam for user interaction and
    a pre-trained model for image prediction. The game involves the user making a hand gesture (Rock, Paper, or Scissors),
    which is captured by the webcam and predicted by the loaded model. The computer randomly selects its choice, and a winner
    is determined based on the user's and computer's choices.
    """
    def get_camera_picture_of_user_action(self):
        """
        Capture user's action via webcam.
        
        Capture the user's hand gesture using the webcam and predict the action using a pre-trained model. Display a countdown
        timer on the screen before capturing the user's action.
        
        Returns:
            np.ndarray: The predicted image data representing the user's action.
        """
        model = load_model('keras_model.h5') # Load the pre-trained model for image prediction
        cap = cv2.VideoCapture(0) # Initialize webcam capture
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        countdown_duration = 5  # Countdown 3 seconds before capturing user's action
        start_time = time.time()
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalise the image
            data[0] = normalized_image
            self.prediction = model.predict(data)
            elapsed_time = time.time() - start_time
            remaining_time = countdown_duration - elapsed_time
            if remaining_time <= 0:
                break
            cv2.imshow('frame', frame)
            print(self.prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to close the window
                break
            print(f"Countdown: {int(remaining_time)} seconds") # Display the countdown
            cv2.putText(frame, f"Countdown: {int(remaining_time)} seconds", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) # Display the countdown on the frame
            cv2.imshow('frame', frame)
            print(self.prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'): # Press q to close the window
                break
        cap.release() # After the loop release the web cam
        cv2.destroyAllWindows() # Then destroy all the windows
        return self.prediction       
    
    def get_prediction(self):
        """
        Get user's predicted choice.

        Get the user's predicted choice based on the image prediction result.

        Returns:
            str: The user's predicted choice (Rock, Paper, or Scissors).
        """
        index_of_user_choice = np.argmax(self.prediction[0])  # Find the index of the maximum predicted value 
        user_action_list = ["Nothing", "Rock", "Paper", "Scissors"]
        self.user_choice = user_action_list[index_of_user_choice]
        return self.user_choice

    def get_computer_choice(self): # randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
        """
        Get Computer's Random Choice.

        Randomly pick an option between Rock, Paper, and Scissors and return the choice.

        Returns:
            str: The computer's randomly chosen action (Rock, Paper, or Scissors).
        """
        computer_action_list = ["Rock", "Paper", "Scissors"]
        self.computer_choice = random.choice(computer_action_list)
        return self.computer_choice

    def get_winner(self): # Checks computers choice vs users and declare a winner
        """
        Determine the winner.

        Compare the user's and computer's choices to determine the winner of the round.

        Returns:
            str: The result of the round (You won!, It is a tie!, or You lost.).
        """
        if self.computer_choice == "Rock" and self.user_choice == "Paper" or self.computer_choice == "Paper" and self.user_choice == "Scissors" or self.computer_choice == "Scissors" and self.user_choice == "Rock":
            return "You won!"
        elif self.computer_choice == self.user_choice:
            return "It is a tie!"
        else:
            return "You lost."
        
    @classmethod
    def play(cls): # Pulls the functions together and plays the RPS game
        """
        Play the Rock-Paper-Scissors game.

        Pulls the functions together and plays the Rock-Paper-Scissors game. The game continues until the specified number
        of wins is achieved by the user or the computer.

        Returns:
            None
        """
        wins_needed = int(input("Enter the number of wins needed to end the game: "))
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
    game = RPS.play() # Start playing the game using the class method