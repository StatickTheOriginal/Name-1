import time
import serial
import json
import os
import logging

class SerialCommandHandler:
    def __init__(self, profile_file, update_active_command_list):
        self.profile_file = profile_file
        self.commands = self.load_commands()
        self.ser = None
        self.com_port = self.load_com_port()
        self.update_active_command_list = update_active_command_list

    def load_com_port(self):
        settings_path = 'settings.json'
        if os.path.isfile(settings_path):
            with open(settings_path, 'r', encoding="utf-8") as f:
                settings = json.load(f)
                return settings.get("com_port", None)
        logging.error("Файл настроек не найден или не содержит COM-порт.")
        return None

    def load_commands(self):
        commands = {}
        try:
            if not os.path.isfile(self.profile_file):
                logging.error(f"Файл '{self.profile_file}' не найден")
                return None

            with open(self.profile_file, 'r', encoding="utf-8") as f:
                profile = json.load(f)
                logging.info(f"Загружен профиль: {self.profile_file}")
                for command in profile.get("commands", []):
                    command_name = command.get("command_name")
                    if command_name:
                        commands[command_name] = {
                            "response": command.get("response", ""),
                            "error": command.get("error", ""),
                            "timeout": command.get("timeout", 0),
                            "emulation_status": profile.get("emulation_status", False)
                        }
                        logging.info(f"Загружена команда: {command_name}")
                    else:
                        logging.warning("Команда без имени в профиле")
            if not commands:
                logging.warning("Список с командами пуст или некорректный")
                return None
            return commands
        except json.JSONDecodeError:
            logging.error(f"Ошибка декодирования JSON в файле '{self.profile_file}'. Проверьте формат файла")
            return None
        except Exception as e:
            logging.error(f"Произошла ошибка при загрузке команд: {e}")
            return None

    def open_port(self):
        if self.com_port is None:
            logging.error("COM-порт не задан.")
            return None

        try:
            self.ser = serial.Serial(self.com_port, baudrate=9600, timeout=1)
            logging.info(f"Выбранный порт ({self.com_port}) открыт.")
            return self.ser
        except serial.SerialException:
            logging.error(f"Не удалось открыть порт {self.com_port}. Пожалуйста, выберите другой порт")
            return None
        except Exception as e:
            logging.error(f"Произошла ошибка при открытии порта: {e}")

    def handle_command(self, request):
        cmd, *params = request.split(".", 1)

        if cmd not in self.commands:
            logging.warning(f"Команда '{cmd}' не существует в словаре")
            return None

        if len(params) > 0:
            logging.info(f"Команда: {cmd}, Параметр: {params[0]}")
        else: 
            logging.info(f"Команда: {cmd}")

        response_info = self.commands[cmd]
        expected_response = response_info.get("response", "")
        expected_error = response_info.get("error", "")
        timeout = response_info.get("timeout", 0)
        emulation_active = response_info.get("emulation_status", False)

        if emulation_active:
            time.sleep(max(timeout / 1000, 0))

        if expected_response:
            response = expected_response + "!"
            logging.info(f"Ответ на команду: {response}")
            return response
        else:
            response = expected_error + "!"
            logging.error(f"Ошибка на команду: {response}")
            return response

    def run(self):
        if self.commands is None:
            logging.error("Команды из файла профиля не загрузились. Завершение работы")
            return

        self.open_port()

        if self.ser is None:
            return

        try:
            while True:
                if self.ser.in_waiting > 0:
                    request = self.ser.readline().decode('utf-8').strip()
                    logging.info(f"Получен запрос: {request}")
                    response = self.handle_command(request)
                    if response:
                        self.ser.write(response.encode('utf-8'))
                        logging.info(f"Отправлен ответ: {response}")
                        self.update_active_command_list(f"Команда: {request}, Результат: {response}")
        except KeyboardInterrupt:
            logging.info("Завершение работы эмулятора")
        except Exception as e:
            logging.error(f"Произошла ошибка во время выполнения: {e}")
        finally:
            if self.ser:
                self.ser.close()
                logging.info("Порт закрыт")

    def stop(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            logging.info("COM-порт закрыт")