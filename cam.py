import cv2
import time
import face_recognition
import os
from load_save import load_save
from face_detection import face_detection

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Erreur : webcam not accessible.")
    exit(1)

BASE_DIR = "face"
ENCODED_FILE = "encodages.pkl"
encodages_connus, noms_connus = load_save(ENCODED_FILE, BASE_DIR)

DELAI_CAPTURE = 1
dernier_temps = time.time()

print("🟢 Surveillance activée. Appuyez sur 'q' pour quitter.")
name = ""

while True:
    ret, frame = cam.read()
    if not ret:
        continue

    petit_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_frame = cv2.cvtColor(petit_frame, cv2.COLOR_BGR2RGB)

    border = (0, 0, 255)
    if (name != "Inconnu" and name != ""):
        border = (0, 255, 0)

    faces = face_recognition.face_locations(rgb_frame)

    if faces:
        dernier_temps = time.time()
        nom_fichier = "capture_detectee.jpg"
        cv2.imwrite(nom_fichier, frame)
        frame = face_detection(nom_fichier, encodages_connus, noms_connus)

    cv2.imshow("Webcam (appuyez sur q pour quitter)", frame)
    cv2.imwrite("web.jpg", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
