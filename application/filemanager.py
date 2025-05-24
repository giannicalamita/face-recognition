from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QStackedWidget, QLabel

class PersonPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()

        back_btn = QPushButton("Retour")
        back_btn.clicked.connect(self.go_back)

        layout.addWidget(QLabel("Ici s'affichera le contenu du dossier 'face'"))
        layout.addWidget(back_btn)
        self.setLayout(layout)

    def go_back(self):
        self.stack.setCurrentIndex(0)  # retourne à la page principale

