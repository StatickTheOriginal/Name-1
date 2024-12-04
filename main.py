from PyQt6.QtWidgets import QApplication

from logic.main_window_logic import MainEmulator

import logging
import sys

logging.basicConfig(level=logging.INFO, filename="emulator_logs.log",
                    encoding='utf-8', filemode="w",
                    format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainEmulator()
    main_window.show()
    sys.exit(app.exec())