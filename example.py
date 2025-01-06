import cv2
import os
import numpy as np

# Create a directory for storing face images
face_dir = 'face_data'
if not os.path.exists(face_dir):
    os.makedirs(face_dir)

# Function to collect face data
def collect_faces(user_id):
    cap = cv2.VideoCapture(0)  # Use the default camera
    count = 0

    while count < 30:  # Collect 30 images
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Save the image
        cv2.imwrite(os.path.join(face_dir, f"user_{user_id}_{count}.jpg"), gray)
        
        count += 1
        cv2.imshow('Collecting Faces', gray)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Function to train the recognizer
def train_recognizer():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    labels = []

    # Iterate through face data directory
    for filename in os.listdir(face_dir):
        if filename.endswith('.jpg'):
            img_path = os.path.join(face_dir, filename)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            label = int(filename.split('_')[1])  # Assuming format user_{label}_{count}.jpg

            faces.append(img)
            labels.append(label)

    recognizer.train(faces, np.array(labels))
    recognizer.save('face_recognizer.yml')
    print("Training complete.")

# Function to recognize faces in a video stream
def recognize_faces():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('face_recognizer.yml')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        detected_faces = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in detected_faces:
            face = gray[y:y+h, x:x+w]
            label, confidence = recognizer.predict(face)
            
            if confidence < 100:  # If confidence is below 100, consider it a match
                name = f"User {label}"
            else:
                name = "Unknown"

            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow('Face Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage:
# First, collect faces for a specific user ID
# collect_faces(user_id=1)

# Then, train the recognizer
# train_recognizer()

# Finally, run face recognition
# recognize_faces()
