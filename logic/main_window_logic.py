from .graphint.main_window import Ui_MainWindow
from .help_list_logic import HelpListWindow
from .settings_logic import SettingsWindow
from .work_emulator_logic import SerialCommandHandler
from .folder_checker import folder_for_profiles_check
from .about_logic import AboutWindow

from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtCore import QStringListModel, QDateTime, pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog

import os
import json
import logging
import threading

class MainEmulator(QMainWindow):
    show_message_signal = pyqtSignal(str, str)

    def __init__(self):
        super(MainEmulator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.show_message_signal.connect(self.show_message)

        folder_for_profiles_check()
        self.load_profiles()

        self.action_list_model = QStringListModel()
        self.ui.listView_action.setModel(self.action_list_model)

        self.active_command_model = QStringListModel()
        self.ui.listView_action.setModel(self.active_command_model)

        self.settings_window = SettingsWindow()
        self.settings_window.settings_updated.connect(self.update_profile_list)

        self.command_processor = None

        self.setup_shortcuts()

        self.setup_buttons()

    def setup_shortcuts(self):
        shortcuts = {
            "Ctrl+I": self.open_about_window,
            "Ctrl+C": self.clear_listView_action,
            "Ctrl+X": self.export_actions,
            "Ctrl+H": self.open_hotkeys,
            "Ctrl+S": self.open_settings,
        }
        for key, action in shortcuts.items():
            shortcut = QShortcut(QKeySequence(key), self)
            shortcut.activated.connect(action)

    def setup_buttons(self):
        self.ui.export_button.clicked.connect(self.export_actions)
        self.ui.help_list_button.clicked.connect(self.open_hotkeys)
        self.ui.settings_button.clicked.connect(self.open_settings)
        self.ui.launch_button.clicked.connect(self.launch_profile_work)
        self.ui.clear_button.clicked.connect(self.clear_listView_action)
        self.ui.stop_button.clicked.connect(self.stop_profile_work)

    def load_profiles(self):
        profiles_folder = 'profiles'
        profiles = []
        self.profiles_dict = {}
        for f in os.listdir(profiles_folder):
            if f.endswith('.json'):
                with open(os.path.join(profiles_folder, f), 'r', encoding='utf-8') as file:
                    try:
                        profile_data = json.load(file)
                        name = profile_data.get('name', f)
                        profiles.append((f, name))
                        self.profiles_dict[name] = f
                    except json.JSONDecodeError:
                        logging.error(f"Ошибка при чтении файла {f}: некорректный формат JSON")
                        QMessageBox.warning(self, "Ошибка загрузки профиля", f"Ошибка при чтении файла {f}: некорректный формат JSON")

        self.ui.profiles_combobox.clear()
        self.ui.profiles_combobox.addItems([name for _, name in profiles])
        logging.info("Список профилей загружен в выпадающий список")

    def clear_listView_action(self):
        logging.info("Кнопка 'Очистить' нажата")
        self.action_list_model.removeRows(0, self.action_list_model.rowCount())
        self.active_command_model.removeRows(0, self.active_command_model.rowCount())

    def export_actions(self):
        options = QFileDialog.Option.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_name:
            try:
                with open(file_name, 'w', encoding='utf-8') as file:
                    for line in self.active_command_model.stringList():
                        file.write(line + '\n')
                QMessageBox.information(self, "Успех", "Данные успешно экспортированы!")
                logging.info("Данные успешно экспортированы в файл: %s", file_name)
            except Exception as e:
                logging.error(f"Ошибка при экспорте данных: {e}")
                QMessageBox.warning(self, "Ошибка", "Не удалось экспортировать данные")

    def update_active_command_list(self, command, response):
        current_list = self.active_command_model.stringList()

        if response == "":
            detailed_message = f"{command} | Время: {QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')}"
        else:
            detailed_message = f"Команда: {command} | Ответ: {response} | Время: {QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss')}"

        current_list.append(detailed_message)
        self.active_command_model.setStringList(current_list)

    def update_profile_list(self):
        self.load_profiles()
        logging.info("Профили в главном окне обновлены")

    def open_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()
        logging.info("Горячие клавиши нажаты")

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
        selected_name = self.ui.profiles_combobox.currentText()
        if selected_name:
            selected_profile = self.profiles_dict.get(selected_name)
            if selected_profile:
                profile_path = os.path.join('profiles', selected_profile)
                self.command_processor = SerialCommandHandler(profile_path, self.update_active_command_list)

                thread = threading.Thread(target=self.run_command_processor)
                thread.start()
            else:
                QMessageBox.warning(self, "Ошибка", "Не удалось найти профиль")
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите профиль")

    def show_message(self, title, message):
        QMessageBox.information(self, title, message)

    def run_command_processor(self):
        try:
            self.command_processor.open_port()
            if self.command_processor.ser is not None:
                self.show_message_signal.emit("Успех", f"COM-порт {self.command_processor.com_port} открыт")
            else:
                self.show_message_signal.emit("Ошибка", "Не удалось открыть COM-порт")

            self.disable_buttons()
            self.command_processor.run()
        except Exception as e:
            logging.error(f"Ошибка при открытии порта: {e}")
            self.show_message_signal.emit("Ошибка", f"Не удалось открыть COM-порт: {self.command_processor.com_port}")
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
        self.ui.export_button.setEnabled(False)
        self.set_button_opacity(0.5)

    def enable_buttons(self):
        self.ui.help_list_button.setEnabled(True)
        self.ui.settings_button.setEnabled(True)
        self.ui.launch_button.setEnabled(True)
        self.ui.clear_button.setEnabled(True)
        self.ui.export_button.setEnabled(True)
        self.set_button_opacity(1.0)

    def set_button_opacity(self, opacity):
        buttons = [
            self.ui.help_list_button,
            self.ui.settings_button,
            self.ui.launch_button,
            self.ui.clear_button,
            self.ui.export_button,
        ]
        for button in buttons:
            button.setStyleSheet(f"opacity: {opacity};")