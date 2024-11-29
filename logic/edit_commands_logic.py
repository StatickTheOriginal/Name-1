from .graphint.edit_commands import Ui_Edit_commands

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow

import logging

class EditCommandWindow(QMainWindow):
    command_updated = pyqtSignal()

    def __init__(self, command_data):
        super(EditCommandWindow, self).__init__()
        self.ui = Ui_Edit_commands()
        self.ui.setupUi(self)

        self.command_data = command_data
        self.load_command()

        self.ui.pushButton_ok.clicked.connect(self.save_and_close_edit_command)
        self.ui.pushButton_cancel.clicked.connect(self.close_edit_command)

    def load_command(self):
        if self.command_data is not None:
            self.ui.lineEdit_command.setText(self.command_data.get("command_name", ""))
            self.ui.lineEdit_response.setText(self.command_data.get("response", ""))
            self.ui.lineEdit_error.setText(self.command_data.get("error", ""))
            timeout_value = self.command_data.get("timeout", 0)
            self.ui.lineEdit_timeout.setText(str(timeout_value) if isinstance(timeout_value, int) else "0")
        else:
            logging.warning("Нет данных команды для загрузки")

    def save_and_close_edit_command(self):
        self.command_data["command_name"] = self.ui.lineEdit_command.text()
        self.command_data["response"] = self.ui.lineEdit_response.text()
        self.command_data["error"] = self.ui.lineEdit_error.text()
        timeout_text = self.ui.lineEdit_timeout.text()
        self.command_data["timeout"] = int(timeout_text) if timeout_text.isdigit() else 0
        self.command_updated.emit()
        logging.info("Команда сохранена. Окно редактирования команды закрыто")
        self.close()

    def close_edit_command(self):
        self.close()
        logging.info("Окно редактирования команды закрыто")