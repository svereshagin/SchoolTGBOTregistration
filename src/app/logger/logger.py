import logging
from pathlib import Path
import json

class JsonLogger:
    """
    JsonLogger - класс для логирования сообщений в формате JSON.

    Этот класс использует стандартный модуль logging для записи логов в файл в формате JSON.

    Attributes:
        log_file (Path): Путь к файлу, в который будут записываться логи.
        logger (Logger): Экземпляр логгера, настроенный для записи в файл.
    """
    def __init__(self, log_file: str):
        """
        Инициализирует JsonLogger.

        Args:
            log_file (str): Путь к файлу, в который будут сохраняться логи.
        """
        self.log_file = Path(log_file)
        self.logger = logging.getLogger("JsonLogger")
        self.logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(self.log_file)
        file_handler.setFormatter(JsonFormatter())
        self.logger.addHandler(file_handler)

    def log(self, level: str, message: str):
        """
        Записывает сообщение в лог с указанным уровнем.

        Args:
            level (str): Уровень логирования ('debug', 'info', 'warning', 'error', 'critical').
            message (str): Сообщение, которое будет записано в лог.
        """
        if level.lower() == 'debug':
            self.logger.debug(message)
        elif level.lower() == 'info':
            self.logger.info(message)
        elif level.lower() == 'warning':
            self.logger.warning(message)
        elif level.lower() == 'error':
            self.logger.error(message)
        elif level.lower() == 'critical':
            self.logger.critical(message)

class JsonFormatter(logging.Formatter):
    """
        JsonFormatter - класс для форматирования логов в формате JSON.

        Этот класс наследуется от logging.Formatter и переопределяет метод format,
        чтобы вернуть запись лога в формате JSON.

        Methods:
            format(record): Форматирует запись лога в формате JSON.
        """
    def format(self, record):
        """
        Форматирует запись лога.

        Args:
            record (LogRecord): Запись лога, которую необходимо отформатировать.

        Returns:
            str: Запись лога в формате JSON.
        """
        log_entry = {
            'level': record.levelname,
            'message': record.getMessage(),
            'time': self.formatTime(record)
        }
        return json.dumps(log_entry)