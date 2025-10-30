import cv2
import os
import time

class FaceDetector:
    def __init__(self):
        # Load OpenCV's pre-trained face detection cascade classifier
        cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        if not os.path.exists(cascade_path):
            raise Exception("❌ Face detection model not found")
        
        self.face_cascade = cv2.CascadeClassifier(cascade_path)
        self.cap = None

    def detect_face(self, timeout_seconds=5):
        """
        Detect face using webcam
        Returns True if face detected, False otherwise
        """
        try:
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Use DirectShow backend
            if not self.cap.isOpened():
                print("❌ Could not access webcam")
                return False

            # Set smaller resolution for faster processing
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

            start_time = time.time()
            while (time.time() - start_time) < timeout_seconds:
                ret, frame = self.cap.read()
                if not ret:
                    continue

                # Convert to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
                )

                if len(faces) > 0:
                    print("✨ Face detected!")
                    return True
                
                time.sleep(0.1)  # Small delay to reduce CPU usage

            print("❌ No face detected in the camera view")
            return False

        except Exception as e:
            print(f"❌ Error in face detection: {str(e)}")
            return False
            
        finally:
            if self.cap is not None:
                self.cap.release()