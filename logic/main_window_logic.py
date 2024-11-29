from .graphint.main_window import Ui_MainWindow

from .help_list_logic import HelpListWindow
from .settings_logic import SettingsWindow
from .work_emulator_logic import SerialCommandHandler
from .folder_checker import folder_for_profiles_check

from PyQt6.QtCore import QStringListModel, QDateTime
from PyQt6.QtWidgets import QMainWindow, QMessageBox

import threading
import logging
import os

# Основной класс эмулятора
class MainEmulator(QMainWindow):
    def __init__(self):
        super(MainEmulator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        folder_for_profiles_check()
        self.load_profiles()

        self.action_list_model = QStringListModel()
        self.ui.listView_action.setModel(self.action_list_model)

        self.active_command_model = QStringListModel()
        self.ui.listView_action.setModel(self.active_command_model)

        self.command_processor = None

        self.ui.help_list_button.clicked.connect(self.open_hotkeys)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.launch_button.clicked.connect(self.launch_profile_work)
        self.ui.clear_button.clicked.connect(self.clear_listView_action)
        self.ui.stop_button.clicked.connect(self.stop_profile_work)

    def load_profiles(self):
        profiles_folder = 'profiles'
        profiles = [f for f in os.listdir(profiles_folder) if f.endswith('.json')]
        self.ui.profiles_combobox.clear()
        self.ui.profiles_combobox.addItems(profiles)
        logging.info("Список профилей загружен в выпадающий список")

    def clear_listView_action(self):
        self.action_list_model.removeRows(0, self.action_list_model.rowCount())

    def update_active_command_list(self, command_result):
        current_list = self.active_command_model.stringList()

        detailed_message = f"Команда выполнена: {command_result} | Время: {QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')}"

        current_list.append(detailed_message)
        self.active_command_model.setStringList(current_list)

    def update_profile_list(self):
        self.load_profiles()
        logging.info("Профили в главном окне обновлены")

    def open_hotkeys(self):
        self.help_window = HelpListWindow()
        self.help_window.show()
        logging.info("Открыто окно с горячими клавишами")

    def open_settings(self):
        self.settings_window = SettingsWindow()
        self.settings_window.profile_added.connect(self.update_profile_list)
        self.settings_window.profile_removed.connect(self.update_profile_list)
        self.settings_window.show()
        logging.info("Открыто окно настроек")

    def launch_profile_work(self):
        selected_profile = self.ui.profiles_combobox.currentText()
        if selected_profile:
            profile_path = os.path.join('profiles', selected_profile)
            self.command_processor = SerialCommandHandler(profile_path, self.update_active_command_list)

            thread = threading.Thread(target=self.run_command_processor)
            thread.start()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите профиль")

    def run_command_processor(self):
        try:
            self.command_processor.open_port()
            self.disable_buttons()
            self.command_processor.run()
        except Exception as e:
            logging.error(f"Ошибка при открытии порта: {e}")
            QMessageBox.warning(self, "Ошибка", f"Не удалось открыть COM-порт: {self.command_processor.com_port}")
        finally:
            self.enable_buttons()

    def stop_profile_work(self):
        if self.command_processor is not None:
            self.command_processor.stop()
            self.command_processor = None
            self.enable_buttons()
        else:
            QMessageBox.warning(self, "Ошибка", "Нет активного профиля для остановки")

    def disable_buttons(self):
        self.ui.help_list_button.setEnabled(False)
        self.ui.settings_button.setEnabled(False)
        self.ui.launch_button.setEnabled(False)
        self.ui.clear_button.setEnabled(False)
        self.ui.help_list_button.setStyleSheet("opacity: 0.5;")
        self.ui.settings_button.setStyleSheet("opacity: 0.5;")
        self.ui.launch_button.setStyleSheet("opacity: 0.5;")
        self.ui.clear_button.setStyleSheet("opacity: 0.5;")

    def enable_buttons(self):
        self.ui.help_list_button.setEnabled(True)
        self.ui.settings_button.setEnabled(True)
        self.ui.launch_button.setEnabled(True)
        self.ui.clear_button.setEnabled(True)
        self.ui.help_list_button.setStyleSheet("")
        self.ui.settings_button.setStyleSheet("")
        self.ui.launch_button.setStyleSheet("")
        self.ui.clear_button.setStyleSheet("")
