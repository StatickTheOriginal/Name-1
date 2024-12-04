from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QStringListModel

from .graphint.help_list import Ui_help_list_window

import logging

class HelpListWindow(QMainWindow):
    def __init__(self):
        super(HelpListWindow, self).__init__()
        self.ui = Ui_help_list_window()
        self.ui.setupUi(self)

        self.listWidget_model = QStringListModel()
        self.ui.listView.setModel(self.listWidget_model)

        hotkeys = [
            "Ctrl+i = Открытие окна about",
            "Ctrl+s = Открытие окна настроек",
            "Ctrl+h = Открытие окна с горячими клавишами",
            "Ctrl+x = Экспорт журнала",
            "Ctrl+c = Очистить журнал"
        ]

        self.listWidget_model.setStringList(hotkeys)

        self.ui.ok_button.clicked.connect(self.close_hotkeys)

    def close_hotkeys(self):
        self.close()
        logging.info("Окно с горячими клавишами закрыто")