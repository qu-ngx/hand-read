# Import libs
import os
import cv2

# Extract from dir data
DATA_DIR = './data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Change the classes when you need to have more gestures
number_of_classes = 24 # Change when you need to have more inputs
dataset_size = 100  # 100 images per folder

cam = cv2.VideoCapture(1)  # Change the number depending on os

# Loop through all the folders
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cam.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)',
                    (100, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.3,
                    (0, 255, 0),
                    3,
                    cv2.LINE_AA)
        # Showing frame by frame
        cv2.imshow('frame', frame)
        # Break when pressing q (Typical OpenCV user =)))))
        if cv2.waitKey(25) == ord('q'):
            break

    # Start counting and making the folder from 0
    counter = 0

    # Looping through folder and creating folder until the cap
    while counter < dataset_size:
        # Reading frame by frame and showing frame then export images into folders
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(
            j), '{}.jpg'.format(counter)), frame)

        counter += 1

cam.release()
cv2.destroyAllWindows()
