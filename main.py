import sys
import sqlite3

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Food Planner")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
