# Aid-for-blind
Aid for the Blind - RAS PESU Major Project (Term: 22-23)

i)Depth Map
#Brief Description of Code:
The model MiDaS_small is loaded from PyTorch, this is responsible for depth prediction
Webcam feed is initialized using cv2 and a loop is entered to process the frames
Each frame read from the webcam is flipped horizontally and converted to RGB color format
Appropriate transformations are applied and passed as input to MiDaS
Depth prediction is interpolated to to original image size, depth prediction is converted to depth map and color mapping is applied
FPS is calculated and rendered on image

#Output:
The code captures real-time webcam frames, processes them through the MiDaS model, and displays both the original image and its depth map side by side. The original image shows the real scene, while the depth map uses a color gradient to represent the depth information. The FPS is displayed on the image. The program can be exited by pressing the 'Esc' key.
