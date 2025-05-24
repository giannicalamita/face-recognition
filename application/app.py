from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from filemanager import PersonPage
from mainpage import MainPage

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Surveillance App")
        self.setGeometry(100, 100, 800, 700)

        self.stack = QStackedWidget(self)

        self.main_page = MainPage(self.stack, self)
        self.file_page1 = PersonPage(self.stack)

        self.stack.addWidget(self.main_page)
        self.stack.addWidget(self.file_page1)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show()
    app.exec_()
