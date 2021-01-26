import os
import cv2
import bios as bi
import faceRecognition as fr
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')
name = {0: "Anmol KC", 1: "Upasna", 2: "Wilson Rai", 3: "Dayahang Rai", 4: "Kabita Ale", 5: "Maotse GRG",
        6: "Bijay Baral", 7: "Puskar Grg"}

"""
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)
"""

face_cascade = cv2.CascadeClassifier(
    r'C:\Users\sanam\Desktop\MovieCharacter\Cascades\haarcascade_frontalface_default.xml')


def get_video():
    cap = cv2.VideoCapture(0)
    while True:
        ret, test_img = cap.read()
        faces_detected, gray_img = fr.faceDetection(test_img)

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)

        resized_img = cv2.resize(test_img, (1000, 700))

        for face in faces_detected:
            (x, y, w, h) = face
            roi_gray = gray_img[y:y + w, x:x + h]
            label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
            print("confidence:", confidence)
            print("label:", label)
            fr.draw_rect(test_img, face)
            predicted_name = name[label]

            if confidence < 50:

                fr.put_text(test_img, predicted_name, x, y)
                cv2.rectangle(test_img, (0, 0), (300, 40), (255, 255, 255), -1)

                if label == 0 and cv2.imwrite != 'Anmol KC.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Anmol KC.jpg',
                        roi_gray)

                if label == 1 and cv2.imwrite != 'Upasna.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Upasna.jpg',
                        roi_gray)

                if label == 2 and cv2.imwrite != 'Wilson Rai.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Wilson Rai.jpg',
                        roi_gray)

                if label == 3 and cv2.imwrite != 'Dayahang Rai.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Dayahang Rai.jpg',
                        roi_gray)

                if label == 4 and cv2.imwrite != 'Kabita Ale.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Kabita Ale.jpg',
                        roi_gray)

                if label == 5 and cv2.imwrite != 'Maotse GRG.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Maotse GRG.jpg',
                        roi_gray)

                if label == 6 and cv2.imwrite != 'Bijay Baral.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Bijay Baral.jpg',
                        roi_gray)

                if label == 7 and cv2.imwrite != 'Puskar Grg.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Puskar Grg.jpg',
                        roi_gray)

        resized_img = cv2.resize(test_img, (1000, 700))

        cv2.imshow('Face Recognition of Character ', resized_img)

        if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Camera Info", "Camera Closed")


def get_file():
    Tk().withdraw()
    filename = askopenfilename()
    cap = cv2.VideoCapture(filename)
    while True:
        ret, test_img = cap.read()
        faces_detected, gray_img = fr.faceDetection(test_img)

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)

        resized_img = cv2.resize(test_img, (1000, 700))

        for face in faces_detected:
            (x, y, w, h) = face
            roi_gray = gray_img[y:y + w, x:x + h]
            label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
            print("confidence:", confidence)
            print("label:", label)
            fr.draw_rect(test_img, face)
            predicted_name = name[label]

            """
			test_image for fram 
			roi_gray for grascale face
			"""

            if confidence < 50:

                fr.put_text(test_img, predicted_name, x, y)

                if label == 0 and cv2.imwrite != 'Anmol KC.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Anmol KC.jpg',
                        roi_gray)

                if label == 1 and cv2.imwrite != 'Upasna.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Upasna.jpg',
                        roi_gray)

                if label == 2 and cv2.imwrite != 'Wilson Rai.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Wilson Rai.jpg',
                        roi_gray)

                if label == 3 and cv2.imwrite != 'Dayahang Rai.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Dayahang Rai.jpg',
                        roi_gray)

                if label == 4 and cv2.imwrite != 'Kabita Ale.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Kabita Ale.jpg',
                        roi_gray)

                if label == 5 and cv2.imwrite != 'Maotse GRG.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Maotse GRG.jpg',
                        roi_gray)

                if label == 6 and cv2.imwrite != 'Bijay Baral.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Bijay Baral.jpg',
                        roi_gray)

                if label == 7 and cv2.imwrite != 'Puskar Grg.jpg':
                    cv2.imwrite(
                        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Puskar Grg.jpg',
                        roi_gray)
        resized_img = cv2.resize(test_img, (1000, 700))

        cv2.imshow('Face Recognition of Character ', resized_img)

        if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
            break

    cap.release()
    cv2.destroyAllWindows()
    messagebox.showinfo("Video Info", "Video Closed")

def get_result():
    root.destroy()
    results = []
    testdir = r"C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized"
    for f in os.listdir(testdir):
        if f.endswith('.jpg'):
            # print()
            results.append(f)
            print(results)
            print("Number of items in the list = ", len(results))

    print("Number of items in the list = ", len(results))

    for s in results:
        if (s == "Anmol KC.jpg"):
            bi.Anmol_bio()
            print("Printed \t" + s)
            #os.remove(r"C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Anmol KC.jpg")

        if (s == "Dayahang Rai.jpg"):
            bi.Daya_bio()
            print("Printed \t" + s)

        if (s == "Kabita Ale.jpg"):
            bi.Kabita_bio()
            print("Printed \t" + s)

        if (s == "Upasna.jpg"):
            bi.Upasna_bio()
            print("Printed \t" + s)

        if (s == "Wilson Rai.jpg"):
            bi.Wilson_bio()
            print("Printed \t" + s)



root = tk.Tk()
root.title("Movie Character Recognizations")
HEIGHT = 700
WIDTH = 800

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Start.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(frame, text="Movie Character Recognization", font=40, bg='white')
label.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=20)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

button = tk.Button(lower_frame, text="Open Camera", bg='#80c1ff', font=40, command=lambda: get_video())
button.place(relx=0.5, rely=0.3, relheight=0.1, relwidth=0.25, anchor='n')

button = tk.Button(lower_frame, text="Open Video", bg='#80c1ff', font=40, command=lambda: get_file())
button.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.25, anchor='n')

button = tk.Button(lower_frame, text="Show Characters", bg='#80c1ff', font=40, command=lambda: get_result())
button.place(relx=0.5, rely=0.7, relheight=0.1, relwidth=0.3, anchor='n')

root.mainloop()
