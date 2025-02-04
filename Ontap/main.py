from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QMessageBox
from PyQt6 import uic
import sys, os

# ============================================================
class ZooList(QMainWindow):
    def __init__(self):
        super().__init__()
        # load ui
        self.ui = uic.loadUi("Ontap/ui/zoo_list.ui", self)
        
        
# ============================================================
class AnimalCard(QWidget):
    pass
# ============================================================
if __name__ == "main":
    app = QApplication(sys.argv)
    zooListWindow = ZooList()
    zooListWindow.show()
    sys.exit(app.exec())