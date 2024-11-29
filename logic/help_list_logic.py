from PyQt6.QtWidgets import QMainWindow

from .graphint.help_list import Ui_help_list_window

import logging

class HelpListWindow(QMainWindow):
    def __init__(self):
        super(HelpListWindow, self).__init__()
        self.ui = Ui_help_list_window()
        self.ui.setupUi(self)

        self.ui.ok_button.clicked.connect(self.close_hotkeys)

    def close_hotkeys(self):
        self.close()
        logging.info("Окно с горячими клавишами закрыто")