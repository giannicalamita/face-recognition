import cv2
import time
import face_recognition
import os
from ..load_save import load_save
from face_detection import face_detection


class record():
    def __init__(self):

        BASE_DIR = "face"
        ENCODED_FILE = "encodages.pkl"
        self.encodages_connus, self.noms_connus = load_save(ENCODED_FILE, BASE_DIR)

        self.DELAI_CAPTURE = 1
        self.dernier_temps = time.time()
        self.cam = cv2.VideoCapture(0)
        self.isRecording = True
        if not self.cam.isOpened():
            self.isRecording = False
            print("Erreur : webcam not accessible.")
            exit(1)
        self.name = ""

    def start(self):
        if not self.isRecording:
            self.cam = cv2.VideoCapture(0)
            self.isRecording = True
            if not self.cam.isOpened():
                self.isRecording = False
                print("Erreur : webcam not accessible.")
                exit(1)
                self.name = ""
        ret, frame = self.cam.read()
        if not ret:
            return
        petit_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(petit_frame, cv2.COLOR_BGR2RGB)

        border = (0, 0, 255)
        if (self.name != "Inconnu" and self.name != ""):
            border = (0, 255, 0)
        faces = face_recognition.face_locations(rgb_frame)
        if faces:
            self.dernier_temps = time.time()
            nom_fichier = "capture_detectee.jpg"
            cv2.imwrite(nom_fichier, frame)
            frame = face_detection(nom_fichier, self.encodages_connus, self.noms_connus)

        # cv2.imshow("Webcam (appuyez sur q pour quitter)", frame)
        self.frame = frame
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop()

    def stop(self):
        if (self.isRecording):
            self.cam.release()
            cv2.destroyAllWindows()
            self.isRecording = False
    def get_frame(self):
        if (self.isRecording):
            return self.frame
        else:
            return None
