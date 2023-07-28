import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('IMAGE.jpg', frame)
        break
cap.release()
cv2.destroyAllWindows()

IMAGE_PATH = 'IMAGE.jpg'

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(IMAGE_PATH)
full_text = ''
for detection in result:
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    full_text += text + ' '
    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)

print(full_text)
text_to_speech(full_text)
plt.imshow(img)
plt.show()