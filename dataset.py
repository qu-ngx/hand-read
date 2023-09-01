
import os
import pickle

import mediapipe as mp
import cv2

# Start drawing hand nodes
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# Stats of a hand
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

DATA_DIR = './data'

# Get input (Set of data) and labels for machine learning
data = []
labels = []

# looping through all the files in directory and start inserting x and y to the dataset (data.pickle)
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):

        # Create a list to store auxilary data (Collecting inputs from the folders of images)
        data_aux = []

        # Setting up x and y to hold the value of x, y when breaking down an image
        x_ = []
        y_ = []

        # Reading each image from directory
        # Read the images from path
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        # Convert the color to RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # store the converted variable
        results = hands.process(img_rgb)

        # Looping through all the hands
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):

                    # Get x and y of hands
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

            data.append(data_aux)
            labels.append(dir_)

# Open data.pickle and add some columns using dump()
f = open('data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)  # Dumping some columns
f.close()
