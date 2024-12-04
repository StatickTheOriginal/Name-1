from .graphint.edit_profiles import Ui_Edit_profiles

from .edit_commands_logic import EditCommandWindow

from PyQt6.QtCore import Qt, QStringListModel, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QMenu

import logging
from datetime import datetime
import os
import json

class EditProfileWindow(QMainWindow):
    profile_updated = pyqtSignal(str)

    def __init__(self, profile_data):
        super(EditProfileWindow, self).__init__()
        self.ui = Ui_Edit_profiles()
        self.ui.setupUi(self)

        self.load_profile_data(profile_data)
        self.load_commands()

        self.ui.pushButton_ok.clicked.connect(self.save_and_close_edit_profile)
        self.ui.pushButton_cancel.clicked.connect(self.close_edit_profile)
        self.ui.pushButton_add_command.clicked.connect(self.add_command)
        self.ui.listView_commands.doubleClicked.connect(self.open_edit_commands)

        self.ui.listView_commands.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.listView_commands.customContextMenuRequested.connect(self.show_context_menu)

    def open_edit_commands(self, index):
        command_name = index.data()
        command_data = next((cmd for cmd in self.profile_data["commands"] if cmd["command_name"] == command_name), None)

        if command_data is not None:
            self.edit_command_window = EditCommandWindow(command_data)
            self.edit_command_window.command_updated.connect(self.load_commands)
            self.edit_command_window.show()
            logging.info(f"Открыто окно редактирования команды: {command_name}")
        else:
            logging.warning(f"Команда не найдена: {command_name}")

    def add_command(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        command_name = f"Command_{timestamp}"
        command_data = {
            "command_name": command_name,
            "response": "",
            "error": "",
            "timeout": 0
        }

        self.profile_data["commands"].append(command_data)
        self.save_profile_data()
        self.load_commands()
        logging.info(f"Создана новая команда: {command_name}")

    def show_context_menu(self, pos):
        context_menu = QMenu(self)
        index = self.ui.listView_commands.indexAt(pos)
        if index.isValid():
            delete_action = context_menu.addAction("Удалить")
            action = context_menu.exec(self.ui.listView_commands.viewport().mapToGlobal(pos))

            if action == delete_action:
                self.delete_command(index.data())

    def delete_command(self, command_name):
        command_data = next((cmd for cmd in self.profile_data["commands"] if cmd["command_name"] == command_name), None)

        if command_data:
            self.profile_data["commands"].remove(command_data)
            self.save_profile_data()
            self.load_commands()
            logging.info(f"Команда {command_name} удалена")
        else:
            logging.warning(f"Команда {command_name} не найдена")

    def load_commands(self):
        commands = self.profile_data.get("commands", [])
        model = QStringListModel()
        model.setStringList([cmd["command_name"] for cmd in commands])
        self.ui.listView_commands.setModel(model)
        logging.info("Список команд загружен")

    def load_profile_data(self, profile_data):
        self.ui.lineEdit_profile_name.setText(profile_data.get("name", ""))
        self.ui.checkBox_work_emulation.setChecked(profile_data.get("emulation_status", False))
        self.profile_data = profile_data

    def save_profile_data(self):
        self.profile_data["name"] = self.ui.lineEdit_profile_name.text()
        self.profile_data["emulation_status"] = self.ui.checkBox_work_emulation.isChecked()

        profile_path = os.path.join('profiles', f"{self.profile_data['name']}.json")
        with open(profile_path, 'w', encoding='utf-8') as f:
            json.dump(self.profile_data, f, ensure_ascii=False, indent=4)

    def save_and_close_edit_profile(self):
        new_profile_name = self.ui.lineEdit_profile_name.text()
        self.profile_data["name"] = new_profile_name
        self.profile_updated.emit(new_profile_name)
        self.save_profile_data()
        self.close()
        logging.info("Профиль сохранён и окно редактирования профилей закрыто")

    def close_edit_profile(self):
        self.close()
        logging.info("Окно редактирования профилей закрыто")