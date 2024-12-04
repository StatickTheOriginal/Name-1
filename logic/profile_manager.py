import os
import json
import logging

from .edit_profile_logic import EditProfileWindow

from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import pyqtSignal, QObject

class ProfileManager(QObject):
    profile_added = pyqtSignal()
    profile_removed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.edit_profile = None
        self.profiles_folder = 'profiles'
        self.check_profiles_folder()

    def check_profiles_folder(self):
        if not os.path.exists(self.profiles_folder):
            os.makedirs(self.profiles_folder)
            logging.info(f"Создана папка профилей: {self.profiles_folder}")

    def load_profiles(self):
        logging.info(f"Проверка наличия папки: {self.profiles_folder}")

        if not os.path.exists(self.profiles_folder):
            logging.error(f"Папка '{self.profiles_folder}' не найдена")
            return []

        profiles_files = [f for f in os.listdir(self.profiles_folder) if f.endswith(".json")]
        logging.info(f"Найденные файлы профилей: {profiles_files}")

        return profiles_files

    def open_edit_profile(self, profile_filename):
        profile_found = False
        profile_data = None

        logging.info(f"Попытка открыть профиль: {profile_filename}")

        profile_path = os.path.join(self.profiles_folder, profile_filename)
        logging.info(f"Проверка файла: {profile_path}")
        try:
            with open(profile_path, 'r', encoding='utf-8') as f:
                profile_data = json.load(f)
                profile_found = True
        except Exception as e:
            logging.error(f"Ошибка при открытии профиля {profile_path}: {e}")

        if profile_found:
            self.edit_window = EditProfileWindow(profile_data)
            self.edit_window.profile_updated.connect(lambda new_name: self.update_profile_name(profile_filename, new_name))
            self.edit_window.show()
            logging.info(f"Открыто окно редактирования профиля: {profile_filename}")
        else:
            logging.warning(f"Профиль с именем файла '{profile_filename}' не найден")
            QMessageBox.warning(None, "Ошибка", f"Профиль с именем файла '{profile_filename}' не найден")

    def delete_profile(self, profile_filename):
        profile_path = os.path.join(self.profiles_folder, profile_filename)

        if os.path.exists(profile_path):
            os.remove(profile_path)
            logging.info(f"Удалён профиль: {profile_filename}")
            self.load_profiles()
        else:
            logging.warning(f"Не удалось удалить профиль, файл не найден с именем: {profile_filename}")
            QMessageBox.warning(None, "Ошибка", f"Не удалось удалить профиль, файл не найден с именем: {profile_filename}")

    def add_profile(self):
        new_profile_number = 1
        while True:
            new_profile_filename = f"profile {new_profile_number}.json"
            new_profile_path = os.path.join(self.profiles_folder, new_profile_filename)
            if not os.path.exists(new_profile_path):
                break
            new_profile_number += 1

        new_profile_name = f"Профиль {new_profile_number}"
        profile_data = {
            "name": new_profile_name,
            "emulation_status": False,
            "EOL_in_end": True,
            "commands": []
        }

        with open(new_profile_path, "w", encoding='utf-8') as f:
            json.dump(profile_data, f, ensure_ascii=False, indent=4)

        self.profile_added.emit()
        logging.info(f"Добавлен новый профиль: {new_profile_path}. Список с профилями обновлён")

    def update_profile_name(self, old_filename, new_name):
        old_profile_path = os.path.join(self.profiles_folder, old_filename)
        new_filename = f"{new_name}.json"
        new_profile_path = os.path.join(self.profiles_folder, new_filename)

        if os.path.exists(old_profile_path):
            if os.path.exists(new_profile_path):
                logging.error(f"Ошибка: файл с именем '{new_filename}' уже существует.")
                QMessageBox.warning(None, "Ошибка", f"Файл с именем '{new_filename}' уже существует. Пожалуйста, выберите другое имя.")
                return

            os.rename(old_profile_path, new_profile_path)
            logging.info(f"Имя профиля обновлено с '{old_filename}' на '{new_filename}'")
            self.profile_added.emit()
        else:
            logging.error(f"Ошибка при обновлении имени профиля: файл '{old_filename}' не найден")