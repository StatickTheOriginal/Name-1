from .graphint.settings import Ui_Settings

from .edit_profile_logic import EditProfileWindow
from .folder_checker import folder_for_profiles_check

from PyQt6.QtCore import Qt, QStringListModel, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QMenu, QMessageBox

import serial
import serial.tools.list_ports
import logging
import json
import os

class SettingsWindow(QMainWindow):
    profile_added = pyqtSignal()
    profile_removed = pyqtSignal()

    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        folder_for_profiles_check()
        self.load_profiles()

        self.ui.ok_button.clicked.connect(self.close_and_save_settings)
        self.ui.cancel_button.clicked.connect(self.close_settings)
        self.ui.add_profile_button.clicked.connect(self.add_profile)
        self.ui.update_COM_ports.clicked.connect(self.available_ports)
        self.ui.listView_profiles.doubleClicked.connect(self.open_edit_profile)

        self.ui.listView_profiles.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.listView_profiles.customContextMenuRequested.connect(self.open_context_menu)

        self.available_ports()

    def available_ports(self):
        self.ui.comboBox_ports.clear()
        ports = serial.tools.list_ports.comports()
        port_list = [port.device for port in ports]
        self.ui.comboBox_ports.addItems(port_list)
        logging.info("Список COM-портов обновлён")

    def close_and_save_settings(self):
        selected_port = self.ui.comboBox_ports.currentText()
        if selected_port:
            settings_path = 'settings.json'
            settings_data = {'com_port': selected_port}
            with open(settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings_data, f, ensure_ascii=False, indent=4)
            logging.info(f"COM-порт {selected_port} сохранён в настройках")
        else:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста, выберите COM-порт")

        self.close_settings()

    def open_edit_profile(self, index):
        profile_name = self.ui.listView_profiles.model().data(index)
        profiles_folder = 'profiles'
        profile_found = False
        profile_data = None

        logging.info(f"Попытка открыть профиль: {profile_name}")

        for filename in os.listdir(profiles_folder):
            if filename.endswith('.json'):
                profile_path = os.path.join(profiles_folder, filename)
                logging.info(f"Проверка файла: {profile_path}")
                try:
                    with open(profile_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if data.get("name") == profile_name:
                            profile_found = True
                            profile_data = data
                            break
                except Exception as e:
                    logging.error(f"Ошибка при открытии профиля {profile_path}: {e}")

        if profile_found:
            self.edit_window = EditProfileWindow(profile_data)
            self.edit_window.profile_updated.connect(self.update_profile_name)
            self.edit_window.show()
            logging.info(f"Открыто окно редактирования профиля: {profile_name}")
        else:
            logging.warning(f"Профиль с именем '{profile_name}' не найден.")
            QMessageBox.warning(self, "Ошибка", f"Профиль с именем '{profile_name}' не найден")

    def open_context_menu(self, position):
        index = self.ui.listView_profiles.indexAt(position)
        if index.isValid():
            menu = QMenu(self)
            delete_action = menu.addAction("Удалить")
            action = menu.exec(self.ui.listView_profiles.viewport().mapToGlobal(position))

            if action == delete_action:
                self.delete_profile(index)

    def delete_profile(self, index):
        profile_name = index.data()
        profiles_folder = 'profiles'
        profile_found = False

        for filename in os.listdir(profiles_folder):
            if filename.endswith('.json'):
                profile_path = os.path.join(profiles_folder, filename)
                try:
                    with open(profile_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if data.get("name") == profile_name:
                            profile_found = True
                            os.remove(profile_path)
                            logging.info(f"Удалён профиль: {profile_name}")
                            break
                except Exception as e:
                    logging.error(f"Ошибка при открытии профиля {profile_path}: {e}")

        if not profile_found:
            logging.warning(f"Не удалось удалить профиль, файл не найден с именем: {profile_name}")
            QMessageBox.warning(self, "Ошибка", f"Не удалось удалить профиль, файл не найден с именем: {profile_name}")

        self.load_profiles()

    def add_profile(self):
        folder_for_profiles_check()

        profiles_folder = 'profiles'
        max_profile_number = len(os.listdir(profiles_folder))
        new_profile_number = max_profile_number + 1
        new_profile_name = f"Профиль {new_profile_number}"
        new_profile_filename = os.path.join(profiles_folder, f"profile {new_profile_number}.json")

        profile_data = {
            "name": new_profile_name,
            "original_name": f"profile {new_profile_number}",
            "emulation_status": False,
            "commands": []
        }

        with open(new_profile_filename, "w", encoding='utf-8') as f:
            json.dump(profile_data, f, ensure_ascii=False, indent=4)

        self.profile_added.emit()
        logging.info(f"Добавлен новый профиль: {new_profile_filename}. Список с профилями обновлён")
        self.load_profiles()

    def update_profile_name(self, new_name):
        index = self.ui.listView_profiles.currentIndex()
        if index.isValid():
            model = self.ui.listView_profiles.model()
            profiles = model.stringList()
            profiles[index.row()] = new_name
            model.setStringList(profiles)
            logging.info(f"Имя профиля обновлено на: {new_name}")

    def load_profiles(self):
        profiles_folder = 'profiles'
        logging.info(f"Проверка наличия папки: {profiles_folder}")

        if not os.path.exists(profiles_folder):
            logging.error(f"Папка '{profiles_folder}' не найдена.")
            return

        profiles_files = [f for f in os.listdir(profiles_folder) if f.endswith(".json")]
        logging.info(f"Найденные файлы профилей: {profiles_files}")

        profiles_names = []

        for profile_file in profiles_files:
            profile_path = os.path.join(profiles_folder, profile_file)
            try:
                with open(profile_path, 'r', encoding='utf-8') as f:
                    profile_data = json.load(f)
                    profiles_names.append(profile_data.get("name", profile_file))
            except json.JSONDecodeError:
                logging.error(f"Ошибка декодирования JSON в файле '{profile_file}'. Проверьте формат файла")
            except Exception as e:
                logging.error(f"Произошла ошибка при загрузке профиля '{profile_file}': {e}")

        model = QStringListModel()
        model.setStringList(profiles_names)
        self.ui.listView_profiles.setModel(model)
        logging.info("Список профилей загружен")

    def close_settings(self):
        self.close()
        logging.info("Окно настроек закрыто")
