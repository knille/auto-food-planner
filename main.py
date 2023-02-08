import sys
import sqlite3

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QTabWidget,
    QWidget,
    QHBoxLayout
)

# class Tabs(QTabWidget):
#     def __init__(self):
#         super().__init__()
# 
#         self.setTabPosition(QTabWidget.TabPosition.West)
# 
#         self.tab_plan_dinner = QWidget()
#         self.tab_add_recipe = QWidget()
#         self.tab_list_all_recipies = QWidget()
# 
#         self.addTab(self.tab_plan_dinner, "Plan dinner")

class PlannedMeals(QWidget):
    """
    This stacked window will display result of planned dinners.
    Connects from tab plan_dinner.
    sent to taskmanager, yes no
    sent to calendar, yes no
    displays meals that have been planned
    """

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Food Planner")
        self.setMinimumSize(QSize(1200, 800))

        tab = QTabWidget()

        # Plan dinner tab
        plan_dinner = QWidget()
        layout = QHBoxLayout()
        plan_dinner.setLayout(layout)
        layout.addWidget(QPushButton("Plan one meal per day"))
        layout.addWidget(QPushButton("Plan two meals per day"))
        
        # Add recipe tab

        # adding tabs
        tab.addTab(plan_dinner, "Plan Dinner")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
