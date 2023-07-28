import pytesseract #recognizes text -> trained model identifies characters in image -> ocnverts to text
import cv2 #image processing
cap = cv2.VideoCapture(0) #initializing the camera
ret, frame = cap.read() #image capturing
cv2.imwrite("image.jpg", frame) #save image
cv2.imshow('Captured image', frame)
cv2.waitKey(0) #wait for keypress before closing window
cap.release()
image = cv2.imread("image.jpg")
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY_INV)[1]
text = pytesseract.image_to_string(threshold)
print(text)