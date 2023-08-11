import cv2
import numpy as np
import random
from keras.models import load_model

number_of_rounds = 5

class RPS():
    def __init__(self, number_of_rounds = 3):
        self.number_of_rounds = number_of_rounds
    
    def get_camera_picture_of_user_action(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            self.prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(self.prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows() 
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
    
def play(): # Pulls the functions together and plays the RPS game
    game = RPS()
    action = game.get_computer_choice()
    game.get_camera_picture_of_user_action()
    choice = game.get_prediction()
    print(f"User's choice: {choice}")
    print(f"Computer's choice: {action}")
    result = game.get_winner()
    print(result)

if __name__ == "__main__":
    play()
