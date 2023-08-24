# Aid-for-blind
Aid for the Blind - RAS PESU Major Project (Term: 22-23)

A software-based aid for blind people, helping them become completely independent by capturing continuous images from the camera and while also gnerating depthmap from the camera attached to the headgear along with a shoulder bag to house the computing unit, battery and electronic components and giving audio information in the earphones. The visually impaired person can perform daily activities more easily. 

## Contributor
* P Vaibhav (PES1UG21CS399)
* Sharanya Patil (PES1UG21CS553)
* Namita Achyuthan (PES1UG22AM100)

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
### Setting up Jetson Nano
Etch Jetson Nano Developer Kit SD Card Image (Refer https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)
### git clone
```git clone https://github.com/IEEE-RAS-PESU/aid-for-blind.git ```
### Install Software Dependencies
```
pip install opencv-python numpy pandas Pillow matplotlib tensorflow tensorflow_hub transformers
pip install speech_recognition subprocess os pyttsx3
pip install face_recognition mediapip
```
### Running the program
Run ```speech_interface.py```
Run ```depthmap.py```

## Program Flow
![Alt text](image link)

## About each subprogram
### i)Depth Map
#### Brief Description of Code:
The model MiDaS_small is loaded from PyTorch, this is responsible for depth prediction
Webcam feed is initialized using cv2 and a loop is entered to process the frames
Each frame read from the webcam is flipped horizontally and converted to RGB color format
Appropriate transformations are applied and passed as input to MiDaS
Depth prediction is interpolated to to original image size, depth prediction is converted to depth map and color mapping is applied
FPS is calculated and rendered on image
#### Output:
The code captures real-time webcam frames, processes them through the MiDaS model, and displays both the original image and its depth map side by side. The original image shows the real scene, while the depth map uses a color gradient to represent the depth information. The FPS is displayed on the image. The program can be exited by pressing the 'Esc' key.
