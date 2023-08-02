import cv2
import numpy as np
from keras.models import load_model
import pyttsx3

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained emotion recognition model
model = load_model('model.h5')

# Define the labels for emotion recognition
labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# Open the default camera
cap = cv2.VideoCapture(0)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    # Read the camera frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop through each face detected
    for (x, y, w, h) in faces:
        # Extract the face ROI
        roi_gray = gray[y:y + h, x:x + w]

        # Resize the face ROI to match the input size of the emotion recognition model
        roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
        roi_gray = roi_gray.astype('float') / 255.0

        # Expand the dimensions of the face ROI to match the input shape of the emotion recognition model
        roi_gray = np.expand_dims(roi_gray, axis=0)
        roi_gray = np.expand_dims(roi_gray, axis=-1)

        # Predict the emotion
        pred = model.predict(roi_gray)[0]
        label = labels[pred.argmax()]

        # Draw a rectangle around the face and display the predicted emotion label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face and Emotion Recognition', frame)

    # Exit the program when 'q' is pressed
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('s'):
        engine.say(f"The current emotion is {label}")
        engine.runAndWait()

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()