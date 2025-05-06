import os
import pickle
import face_recognition

def load_save(ENCODED_FILE, BASE_DIR, recreate=False):
    if os.path.exists(ENCODED_FILE) and not recreate:
        with open(ENCODED_FILE, "rb") as f:
            return pickle.load(f)
    else:
        encodages_connus = []
        noms_connus = []

        for personne in os.listdir(BASE_DIR):
            dossier = os.path.join(BASE_DIR, personne)
            if not os.path.isdir(dossier):
                continue

            for photo in os.listdir(dossier):
                chemin_photo = os.path.join(dossier, photo)
                image = face_recognition.load_image_file(chemin_photo)
                enc = face_recognition.face_encodings(image)
                if enc:
                    encodages_connus.append(enc[0])
                    noms_connus.append(personne)

        with open(ENCODED_FILE, "wb") as f:
            pickle.dump((encodages_connus, noms_connus), f)
        return load_save(ENCODED_FILE, BASE_DIR)
