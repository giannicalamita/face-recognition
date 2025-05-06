import face_recognition
import cv2
import os
import sys
from load_save import load_save
from face_detection import face_detection

if len(sys.argv) < 2:
    print("Usage : python main.py [filepath]")
    sys.exit(1)

IMAGE_TEST = sys.argv[1]

BASE_DIR = "face"
ENCODED_FILE = "encodages.pkl"

if not os.path.isfile(IMAGE_TEST):
    print(f"File not found : {IMAGE_TEST}")
    sys.exit(1)
if not os.path.isdir(BASE_DIR):
    print(f"Base directory not found: {BASE_DIR}")
    sys.exit(1)

recreate = False
if (sys.argv.count("-r") > 0 or sys.argv.count("--recreate") > 0):
    recreate = True
encodages_connus, noms_connus = load_save(ENCODED_FILE, BASE_DIR, recreate)

image = face_detection(IMAGE_TEST, encodages_connus, noms_connus)

cv2.imshow("Résultat", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
