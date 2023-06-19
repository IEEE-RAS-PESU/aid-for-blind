import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

from gtts import gTTS
import os
def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text)

    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)

    # Play the audio file
    os.system('start ' + speech_file)


IMAGE_PATH = 'sign.png'
#IMAGE_PATH = 'surf.jpeg'

reader = easyocr.Reader(['en'])
result = reader.readtext(IMAGE_PATH)

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

"""img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
img = cv2.putText(img,text,top_left, font, 0.5,(255,255,255),2,cv2.LINE_AA)
plt.imshow(img)
plt.show()
"""

img = cv2.imread(IMAGE_PATH)
full_text=''
for detection in result: 
    top_left = tuple(detection[0][0])
    bottom_right = tuple(detection[0][2])
    text = detection[1]
    full_text+=text+' '
    img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)

print(full_text)
text_to_speech(full_text)
plt.imshow(img)
plt.show()