import cv2
import random
import numpy as np
from keras.models import load_model 

model = load_model('keras_model.h5') # load_model is used to load a pre-trained Keras model from a saved file (HDF5 format with a .h5 extension).
cap = cv2.VideoCapture(0) # initializes a video capture, capturing video frames from the default camera on your computer.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32) # Creating NumPy array with specific shape and data type.

def get_computer_choice(): # randomly pick an option between "Rock", "Paper", and "Scissors" and return the choice
    action_list = ["Rock", "Paper", "Scissors"]
    action = random.choice(action_list)
    return action

def input():
    while True:
        ret, frame = cap.read() # Capture a frame from the camera
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA) # Capture a frame from the camera
        image_np = np.array(resized_frame)  # Convert the resized frame to a NumPy array
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the pixel values of the image to be in the range [-1, 1]
        data[0] = normalized_image # Assign the normalized image data to the 'data' array for prediction
        return ret, frame, resized_frame, image_np, normalized_image, data[0]

def cleans():
    while True:
        print(data[0]) ### Remove this after
        return data[0]

def output():
    while True:
        prediction = model.predict(data) # Make a prediction using the pre-trained deep learning model
        cv2.imshow('frame', frame) # Display the original frame in a window named 'frame'
        # Press q to close the window
        print(prediction) # Print the prediction probabilities for each class
        if cv2.waitKey(1) & 0xFF == ord('q'): # Check if the 'q' key is pressed; if so, exit the loop
            break
        return  

def get_prediction():
    input()
    cleans()
    output()
    return 

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()


'''This question can be answered from the technical perspective, or from a perspective that wants to keep a code 
clean and friendly user. Let's start with the possible technical issues If you can't turn your code into a function, 
make sure you are following the right syntax: use the "def" keyword, use parentheses to define the arguments if any, 
don't forget the colon, and then, don't forget the right indentation Now, if you want to create a function to make 
your code cleaner and nicer, there is a very good principle for that: separation of concerns. Your function should 
do something tangible, with a specific use. For example, a function that downloads, cleans, and uploads data does 
too many things. It would be worth separating it into its concerns: one function for downloading data, another for 
cleaning data, and another for uploading data. That way, it will be easier to do these three things separately, and 
at the same time, doing all three in sequence won't affect the performance of the code'''


def get_winner(computer_choice, user_choice): # Checks computers choice vs users and declare a winner
    if computer_choice == "Rock" and user_choice == "Paper" or computer_choice == "Paper" and user_choice == "Scissors" or computer_choice == "Scissors" and user_choice == "Rock":
        return "You won!"
    elif computer_choice == "Rock" and user_choice == "Scissors" or computer_choice == "Paper" and user_choice == "Rock" or computer_choice == "Scissors" and user_choice == "Paper":
        return "You lost."
    else:
        return "It is a tie!"

def play(): # Pulls the functions together and plays the RPS game
    action = get_computer_choice()
    choice = get_user_choice()
    print(f"Computer's choice: {action}")
    result = get_winner(action, choice)
    print(result)

if __name__ == "__main__":
    play()
