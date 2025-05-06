import face_recognition
import os
import cv2

# === Chargement de la base de données ===
chemin_base = "face"
encodages_connus = []
noms_connus = []

# Parcours des dossiers dans "face"
for nom_personne in os.listdir(chemin_base):
    chemin_personne = os.path.join(chemin_base, nom_personne)
    
    if not os.path.isdir(chemin_personne):
        continue

    for fichier in os.listdir(chemin_personne):
        chemin_photo = os.path.join(chemin_personne, fichier)
        image = face_recognition.load_image_file(chemin_photo)
        encodages = face_recognition.face_encodings(image)
        
        if encodages:
            encodages_connus.append(encodages[0])
            noms_connus.append(nom_personne)

# === Analyse de la photo à vérifier ===
image_test = face_recognition.load_image_file("test/6.jpg")
locations = face_recognition.face_locations(image_test)
encodages_test = face_recognition.face_encodings(image_test, locations)

print("demmarage")
# === Comparaison ===
for (top, right, bottom, left), encoding in zip(locations, encodages_test):
    correspondances = face_recognition.compare_faces(encodages_connus, encoding)
    nom_detecte = "Inconnu"

    if True in correspondances:
        index = correspondances.index(True)
        nom_detecte = noms_connus[index]

    print(f"Visage détecté : {nom_detecte}")
