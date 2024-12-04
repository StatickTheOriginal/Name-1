from .graphint.settings import Ui_Settings
from .folder_checker import folder_for_profiles_check
from .profile_manager import ProfileManager

from PyQt6.QtCore import Qt, pyqtSignal, QStringListModel
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QMenu

import serial.tools.list_ports
import logging
import json
import os

class SettingsWindow(QMainWindow):
    profile_added = pyqtSignal()
    profile_removed = pyqtSignal()
    settings_updated = pyqtSignal()

    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        folder_for_profiles_check()
        self.profile_manager = ProfileManager()
        self.load_profiles()

        self.ui.ok_button.clicked.connect(self.close_and_save_settings)
        self.ui.cancel_button.clicked.connect(self.close_settings)
        self.ui.add_profile_button.clicked.connect(self.add_profile)
        self.ui.update_COM_ports.clicked.connect(self.available_ports)

        self.ui.listView_profiles.doubleClicked.connect(self.open_edit_profile)

        self.ui.listView_profiles.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.listView_profiles.customContextMenuRequested.connect(self.open_context_menu)

        self.available_ports()
        self.load_settings()

    def available_ports(self):
        self.ui.comboBox_ports.clear()
        ports = serial.tools.list_ports.comports()
        port_list = [port.device for port in ports]
        self.ui.comboBox_ports.addItems(port_list)
        logging.info("Список COM-портов обновлён")

    def update_profiles_list(self):
        profiles_names = self.profile_manager.load_profiles()
        model = QStringListModel()
        model.setStringList(profiles_names)
        self.ui.listView_profiles.setModel(model)
        logging.info("Список профилей обновлён после изменения имени")

    def load_settings(self):
        settings_path = 'settings.json'
        if os.path.exists(settings_path):
            try:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    settings_data = json.load(f)
                    com_port = settings_data.get('com_port')
                    if com_port:
                        if com_port in [self.ui.comboBox_ports.itemText(i) for i in range(self.ui.comboBox_ports.count())]:
                            self.ui.comboBox_ports.setCurrentText(com_port)
                            logging.info(f"Загружен COM-порт: {com_port}")
                        else:
                            logging.warning(f"COM-порт '{com_port}' не найден в списке доступных портов")
            except Exception as e:
                logging.error(f"Ошибка при загрузке настроек из файла '{settings_path}': {e}")

    def close_and_save_settings(self):
        selected_port = self.ui.comboBox_ports.currentText()
        if selected_port:
            settings_path = 'settings.json'
            settings_data = {'com_port': selected_port}
            with open(settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings_data, f, ensure_ascii=False, indent=4)
            logging.info(f"COM-порт {selected_port} сохранён в настройках")
            QMessageBox.information(self, "Информация", f"Сохранённый COM-порт: {selected_port}")
        else:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите COM-порт")

        self.settings_updated.emit()
        self.close_settings()

    def open_edit_profile(self, index):
        profile_name = self.ui.listView_profiles.model().data(index)
        if profile_name:
            self.profile_manager.open_edit_profile(profile_name)
            self.profile_manager.profile_added.connect(self.update_profiles_list)
        else:
            QMessageBox.warning(self, "Ошибка", "Не удалось открыть профиль. Имя профиля пустое")

    def open_context_menu(self, position):
        index = self.ui.listView_profiles.indexAt(position)
        if index.isValid():
            profile_name = self.ui.listView_profiles.model().data(index)
            menu = QMenu(self)
            delete_action = menu.addAction("Удалить")
            action = menu.exec(self.ui.listView_profiles.viewport().mapToGlobal(position))

            if action == delete_action:
                self.profile_manager.delete_profile(profile_name)
                self.load_profiles()

    def add_profile(self):
        self.profile_manager.add_profile()
        self.load_profiles()

    def load_profiles(self):
        profiles_names = self.profile_manager.load_profiles()
        model = QStringListModel()
        model.setStringList(profiles_names)
        self.ui.listView_profiles.setModel(model)
        logging.info("Список профилей загружен")

    def close_settings(self):
        self.close()
        logging.info("Окно настроек закрыто")