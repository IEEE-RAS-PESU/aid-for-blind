import speech_recognition as sr
import subprocess
import os

def run_program_in_different_directory(program_path, directory_path):
    os.chdir(directory_path)
    try:
        # Run the Python program using the subprocess module
        subprocess.run(['python', program_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    finally:
        # Change the current working directory back to the original directory
        os.chdir(os.path.dirname(os.path.realpath(__file__)))

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize the speech
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "run" in command:
                file_name = command.replace("run", "").strip()


                if file_name=="hand gesture":
                    program_path = r"C:\Users\vaibhav\Desktop\PES Super File\cRAIS\hand_gesture_recognition_working\hand_gesture_detection.py"
                    directory_path = r"C:\Users\vaibhav\Desktop\PES Super File\cRAIS\hand_gesture_recognition_working"
                    run_program_in_different_directory(program_path, directory_path)

                if file_name=="emotion recognition":
                    program_path = r"C:\Users\vaibhav\Desktop\PES Super File\cRAIS\emotion_recognition\emotion_recognition.py"
                    directory_path = r"C:\Users\vaibhav\Desktop\PES Super File\cRAIS\emotion_recognition"
                    run_program_in_different_directory(program_path, directory_path)

                if file_name=="text recognition":
                    program_path = r"C:\Users\vaibhav\Desktop\PES Super File\cRAIS\text_recognition\ocr_for_cam.py"
                    directory_path = r"C:\Users\vaibhav\Desktop\PES Super File\cRAIS\text_recognition"
                    run_program_in_different_directory(program_path, directory_path)          

            else:
                print("Sorry, I couldn't understand the command.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the speech.")
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")

if __name__ == "__main__":
    main()