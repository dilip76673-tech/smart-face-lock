import cv2
import time
import ctypes
from face_utils import train_model, recognize_face
from voice_alert import speak_access_failed

AUTHORIZED_FACE_DIR = "authorized_face"

def lock_windows():
    ctypes.windll.user32.LockWorkStation()

def main():
    recognizer, face_cascade = train_model(AUTHORIZED_FACE_DIR)

    cam = cv2.VideoCapture(0)

    unauthorized_count = 0
    missing_count = 0   # ← YAHI PE

    print("System started. Monitoring user...")


    while True:
        ret, frame = cam.read()
        if not ret:
            break

        authorized = recognize_face(frame, recognizer, face_cascade)

        if authorized is True:
            unauthorized_count = 0
            missing_count = 0
            status = "AUTHORIZED"
            color = (0, 255, 0)

        elif authorized is None:
            missing_count += 1
            status = "FACE NOT CLEAR"
            color = (0, 255, 255)

        else:
            unauthorized_count += 1
            status = "UNAUTHORIZED"
            color = (0, 0, 255)

        cv2.putText(
            frame,
            status,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )

        cv2.imshow("Smart Laptop Lock", frame)

        # sirf tab lock jab 4 sec tak continuously unauthorized ho
        if unauthorized_count > 80:
            speak_access_failed()
            lock_windows()
            break

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
