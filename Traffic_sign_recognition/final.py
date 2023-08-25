import numpy as np
import cv2
import pickle

frame_width = 640
frame_height = 480
brightness_level = 180
confidence_threshold = 0.75
font_type = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, brightness_level)

pickle_file = open("model_trained.p", "rb")
loaded_model = pickle.load(pickle_file)

def convert_to_grayscale(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image

def apply_histogram_equalization(image):
    equalized_image = cv2.equalizeHist(image)
    return equalized_image

def preprocess_image(image):
    gray_image = convert_to_grayscale(image)
    equalized_image = apply_histogram_equalization(gray_image)
    normalized_image = equalized_image / 255
    return normalized_image

def getClassName(classNo):
    if   classNo == 0: return 'Speed Limit 20 km/h'
    elif classNo == 1: return 'Speed Limit 30 km/h'
    elif classNo == 2: return 'Speed Limit 50 km/h'
    elif classNo == 3: return 'Speed Limit 60 km/h'
    elif classNo == 4: return 'Speed Limit 70 km/h'
    elif classNo == 5: return 'Speed Limit 80 km/h'
    elif classNo == 6: return 'End of Speed Limit 80 km/h'
    elif classNo == 7: return 'Speed Limit 100 km/h'
    elif classNo == 8: return 'Speed Limit 120 km/h'
    elif classNo == 9: return 'No passing'
    elif classNo == 10: return 'No passing for vechiles over 3.5 metric tons'
    elif classNo == 11: return 'Right-of-way at the next intersection'
    elif classNo == 12: return 'Priority road'
    elif classNo == 13: return 'Yield'
    elif classNo == 14: return 'Stop'
    elif classNo == 15: return 'No vechiles'
    elif classNo == 16: return 'Vechiles over 3.5 metric tons prohibited'
    elif classNo == 17: return 'No entry'
    elif classNo == 18: return 'General caution'
    elif classNo == 19: return 'Dangerous curve to the left'
    elif classNo == 20: return 'Dangerous curve to the right'
    elif classNo == 21: return 'Double curve'
    elif classNo == 22: return 'Bumpy road'
    elif classNo == 23: return 'Slippery road'
    elif classNo == 24: return 'Road narrows on the right'
    elif classNo == 25: return 'Road work'
    elif classNo == 26: return 'Traffic signals'
    elif classNo == 27: return 'Pedestrians'
    elif classNo == 28: return 'Children crossing'
    elif classNo == 29: return 'Bicycles crossing'
    elif classNo == 30: return 'Beware of ice/snow'
    elif classNo == 31: return 'Wild animals crossing'
    elif classNo == 32: return 'End of all speed and passing limits'
    elif classNo == 33: return 'Turn right ahead'
    elif classNo == 34: return 'Turn left ahead'
    elif classNo == 35: return 'Ahead only'
    elif classNo == 36: return 'Go straight or right'
    elif classNo == 37: return 'Go straight or left'
    elif classNo == 38: return 'Keep right'
    elif classNo == 39: return 'Keep left'
    elif classNo == 40: return 'Roundabout mandatory'
    elif classNo == 41: return 'End of no passing'
    elif classNo == 42: return 'End of no passing by vechiles over 3.5 metric tons'
    
while True:
    success, original_image = cap.read()

    image = np.asarray(original_image)
    image = cv2.resize(image, (32, 32))
    preprocessed_image = preprocess_image(image)

    original_image = cv2.resize(original_image, (800, 600))

    cv2.imshow("Processed Image", preprocessed_image)
    preprocessed_image = preprocessed_image.reshape(1, 32, 32, 1)
    cv2.putText(original_image, "CLASS: ", (20, 35), font_type, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(original_image, "PROBABILITY: ", (20, 75), font_type, 0.75, (0, 0, 255), 2, cv2.LINE_AA)

    predictions = loaded_model.predict(preprocessed_image)
    class_index = np.argmax(predictions)
    probability_value = np.amax(predictions)

    if probability_value > confidence_threshold:
        class_name = get_class_name(class_index)
        cv2.putText(original_image, str(class_index) + " " + class_name, (120, 35), font_type, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(original_image, str(round(probability_value * 100, 2)) + "%", (180, 75), font_type, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("Result", original_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
