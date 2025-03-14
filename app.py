import sys
from PyQt6.QtWidgets import QApplication
from ui.ui_main import MainUI

def main():
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
