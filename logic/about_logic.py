from .graphint.about import Ui_MainAboutWindow

from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtCore import QStringListModel, QDateTime
from PyQt6.QtWidgets import QMainWindow, QMessageBox

import logging

class AboutWindow(QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.ui = Ui_MainAboutWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_ok.clicked.connect(self.close_about)

    def close_about(self):
        self.close()
        logging.info("Кнопка в окне об программе нажата")