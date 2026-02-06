import cv2
import os
import numpy as np

CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

def train_model(authorized_face_dir):
    faces = []
    labels = []

    face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

    for file in os.listdir(authorized_face_dir):
        if file.lower().endswith((".jpg", ".png")):
            img_path = os.path.join(authorized_face_dir, file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            detected = face_cascade.detectMultiScale(img, 1.3, 5)
            for (x, y, w, h) in detected:
                faces.append(img[y:y+h, x:x+w])
                labels.append(0)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))
    return recognizer, face_cascade


def recognize_face(frame, recognizer, face_cascade, threshold=85):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None  # face temporarily not visible

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi)

        if confidence < threshold:
            return True   # authorized
        else:
            return False  # unauthorized

    return None