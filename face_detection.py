import face_recognition
import cv2

def face_detection(IMAGE_TEST, encodages_connus, noms_connus):
    image = cv2.imread(IMAGE_TEST)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb_image)
    encodages = face_recognition.face_encodings(rgb_image, locations)

    for (top, right, bottom, left), enc in zip(locations, encodages):
        matches = face_recognition.compare_faces(encodages_connus, enc)
        nom = "Inconnu"
        couleur = (0, 0, 255)

        if True in matches:
            idx = matches.index(True)
            nom = noms_connus[idx]
            couleur = (255, 0, 0)

        cv2.rectangle(image, (left, top), (right, bottom), couleur, 2)
        cv2.rectangle(image, (left, bottom - 20), (right, bottom), couleur, cv2.FILLED)
        cv2.putText(image, nom, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    return image

def face_detection_name(IMAGE_TEST, encodages_connus, noms_connus):
    image = cv2.imread(IMAGE_TEST)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    locations = face_recognition.face_locations(rgb_image)
    encodages = face_recognition.face_encodings(rgb_image, locations)

    results = []
    for (top, right, bottom, left), enc in zip(locations, encodages):
        matches = face_recognition.compare_faces(encodages_connus, enc)
        nom = "Inconnu"

        if True in matches:
            idx = matches.index(True)
            nom = noms_connus[idx]

            results.append({"nom": nom, "top": top, "right": right, "bottom": bottom, "left": left})
    return results