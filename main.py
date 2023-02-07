import sys
import sqlite3

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QTabWidget,
    QWidget
)

from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Food Planner")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(False)

        tabs.addTab()

        # tabs.addTab(QTabWidget.setTabText(0, "Plan dinner"))
        # tabs.addTab.setTabText(1, "Add recipe")
        # tabs.addTab.setTabText(2, "All recipies")

        self.setCentralWidget(tabs)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
