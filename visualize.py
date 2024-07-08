import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Train Simulation")

        self.train_coords = {}  # Dictionary to store train coordinates

        # Map background (replace with your actual map image)
        self.map_pixmap = QPixmap("map.png")

        # Set up timer to update train positions periodically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_trains)
        self.timer.start(1000)  # Update every second

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.map_pixmap)
        pen = QPen(QColor(Qt.red), 5)  # Thick red line
        painter.setPen(pen)
        for train_id, coords in self.train_coords.items():
            painter.drawLine(*coords)

    def update_trains(self):
        for train_id, coords in generate_coordinates("timetable.xml"):
            self.train_coords[train_id] = coords
        self.update()  # Trigger repaint

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
