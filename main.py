import sys
from PyQt5.QtWidgets import QApplication
import gui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    _ = gui.MainWindow()
    sys.exit(app.exec())
