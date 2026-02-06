# smart-face-lock
# smart-face-lock

# 🔐 Smart Face Lock System

A Python-based smart laptop/door lock system that uses **real-time face recognition**
to allow access only to authorized users.

---

## 📌 Project Overview
The Smart Face Lock System enhances security by using a camera to detect and recognize
faces. If the detected face matches the trained authorized user, access is granted;
otherwise, access is denied with a voice alert.

This project demonstrates the practical use of **Computer Vision** and **AI**
in real-world security systems.

---

## ⚙️ How It Works
1. Camera captures live video feed  
2. Face is detected using Haar Cascade  
3. Face is compared with trained authorized data  
4. ✅ If authorized → Access granted  
5. ❌ If unauthorized → Access denied + voice alert  

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- Haar Cascade Classifier  
- Text-to-Speech (Voice Alert)  

---

## 📂 Project Structure

smart-face-lock/ │── main.py              # Main execution file │── face_utils.py        # Face detection & recognition logic │── voice_alert.py       # Voice alert for access result │── authorized_face/     # Authorized user images │── trainer/             # Trained face data │── requirements.txt     # Required libraries │── README.md


🚀 Features
Real-time face detection
Authorized vs Unauthorized user recognition
Voice alert system
Simple and efficient d


👨‍💻 Author
Dilip kumar
B.Tech CSE Student
