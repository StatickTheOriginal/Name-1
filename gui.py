import sys
import os
from PyQt6.QtWidgets import QApplication
from logic.main_window_logic import MainEmulator


current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainEmulator()
    main_window.show()
    sys.exit(app.exec())