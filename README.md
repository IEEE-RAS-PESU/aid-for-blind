# Aid-for-blind
Aid for the Blind - RAS PESU Major Project (Term: 22-23)

A software-based aid for blind people, helping them become completely independent by capturing continuous images from the camera and while also gnerating depthmap from the camera attached to the headgear along with a shoulder bag to house the computing unit, battery and electronic components and giving audio information in the earphones. The visually impaired person can perform daily activities more easily. 

## Contributor
* P Vaibhav (PES1UG21CS399)
* Sharanya Patil (PES1UG21CS553)
* Namita Achyuthan (PES1UG22AM100)

### Mentor
* Srividya Prasad (PES1UG21EC297) 

## Technologies Used
* Depth Estimation - MiDaS
* Basic Image Captioning - AlexNet,GoogleNet, ResNet, VGG 
* Object_Recognition - SSDModbileNet2
* Face recognition - Haarcascade and Face recognition modules
* Hand Gesture recognition - Mediapipe
* Optical Character Recognition - EasyOCR, pyttsx3
* Emotion recognition - Haarcascade 
* Speech interface – Speech Recognition module
* Traffic Sign Recognition - PIL
* Navigation - geocoding API


## Installation
### Hardware Requirements
* Jetson Nano
* microSD card (32GB UHS-1 minimum recommended)
* USB keyboard and mouse
* Computer display (HDMI or DP)
* Micro-USB power supply
* Headphones with mic
### Setting up Jetson Nano
Etch Jetson Nano Developer Kit SD Card Image (Refer https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)
### Clone Repository
```git clone https://github.com/IEEE-RAS-PESU/aid-for-blind.git ```
### Install Software Dependencies
```
pip install opencv-python numpy pandas Pillow matplotlib tensorflow tensorflow_hub transformers
pip install speech_recognition subprocess os pyttsx3
pip install face_recognition mediapip
```
### Running the program
* Change the location of programs in ```speech_interface.py``` to match the directories in your system
* Run ```speech_interface.py```
* Run ```depthmap.py```
* To run any of the program say "run ```program name```"

## Program Flow
![Program_Flow](https://github.com/IEEE-RAS-PESU/aid-for-blind/assets/65724191/1095967a-ea6c-4b14-9cb9-4806a6bc0469)
