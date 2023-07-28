'''
#Text input from user
import googlemaps
#initialize API client
gmap = googlemaps.Client(api_key = "API_KEY_GOES_HERE")
#current location
cur_loc = gmap.geocode('Current location')[0]('location')
dest = input("Enter your destination: ")
#get directions
directions = gmap.directions(cur_loc, dest)
for step in directions['steps']:
    print(step['instructions'])'''

#Destination input from user in the form of an image
import googlemaps
import pytesseract
from gtts import gTTS
import os
gmap = googlemaps.Client(api_key = "API_KEY_GOES_HERE")
text = pytesseract.image_to_string('image.jpg')
cur_loc = gmap.geocode('Current location')[0]('location')
dest = text.split('to')[1].strip()
directions = gmap.directions(cur_loc, dest)
for step in directions['steps']:
    text = step['instructions']
    language = 'en'
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save("text.mp3")
    os.system("start text.mp3")