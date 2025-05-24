from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
import cv2
from record import record

class MainPage(QWidget):
    def __init__(self, stack, mainWindow):
        super().__init__()
        self.stack = stack
        self.mainWindow = mainWindow
        self.layout = QVBoxLayout()


        btn_personne = QPushButton("📸 Manage pictures know")
        btn_personne.clicked.connect(self.goto_person_page)

        self.layout.addWidget(btn_personne)

        self.isFilming = False
        self.btn_start = QPushButton("🎥 Start camera")
        self.btn_stop = QPushButton("⏪ Stop camera")
        self.btn_quit = QPushButton("❌ Exit")

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.btn_start)
        self.layout.addWidget(self.btn_stop)
        self.btn_stop.hide()
        self.layout.addWidget(self.btn_quit)

        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.btn_start.clicked.connect(self.start_camera)
        self.btn_stop.clicked.connect(self.stop_camera)
        self.btn_quit.clicked.connect(self.close)
        self.setLayout(self.layout)

        self.record = record()

    def goto_person_page(self):
        self.stack.setCurrentIndex(1) 

    def start_camera(self):
        # self.cap = cv2.VideoCapture(0)
        self.record.start()
        # self.timer.start(30)
        self.isFilming = True
        self.btn_start.hide()
        self.btn_stop.show()

    def update_frame(self):
        if (self.record.isRecording):
            frame = self.record.get_frame()
            if frame is not None:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                pix = QPixmap.fromImage(img)
                self.image_label.setPixmap(pix)
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            pix = QPixmap.fromImage(img)
            self.image_label.setPixmap(pix)

    def stop_camera(self):
        self.timer.stop()
        if self.cap:
            self.cap.release()
        self.image_label.clear()
        self.isFilming = False
        self.btn_start.show()
        self.btn_stop.hide()

    def closeEvent(self, event):
        self.stop_camera()
        self.layout.replaceWidget(self.btn_stop, self.btn_start)
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to exit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No) 
        if reply == QMessageBox.Yes:
            self.mainWindow.close()
        else:
            event.ignore()
        event.accept()