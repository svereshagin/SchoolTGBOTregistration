from pathlib import Path
import yaml
from src.app.logger.logger import JsonLogger
from telebot import TeleBot, types
from src.bot_instance import bot
from pydantic import BaseModel


class TelebotCommand(BaseModel):
    command: str
    description: str


class Keyboard_path_manager:
    """Класс для работы с клавиатурой в telegram чате
       Опционально можете передать путь относительно текущей директории
       Standart: _path_to_file.
    """
    _path_to_file = Path(__file__).parent / "keyboards.yml"  # Одинарное подчеркивание
    logger = JsonLogger("logs.json")

    def __init__(self, path=None):
        if path:
            self.path = path
        print(self._path_to_file)

    @property
    def path(self):
        return self._path_to_file

    @path.setter
    def path(self, new_path: str) -> None:
        """Устанавливает новый путь к файлу, если он существует
        относительно текущей директории

        Args:
            new_path (str): Новый путь к файлу.
        """
        new_path = Path(new_path)
        if new_path.is_file() and new_path.suffix == '.yml':
            self._path_to_file = new_path
            self.logger.log('info', f'Path updated to {new_path}')
        else:
            error_message = f"Invalid file path: {new_path}. File must exist and have a '.yml' extension."
            self.logger.log('error', error_message)
            raise ValueError(error_message)  # Выбрасываем исключение для обработки в вызывающем коде

    def read_yml(self):
        try:
            with open(self.path, "r", encoding='UTF-8') as ymlfile:
                data = yaml.safe_load(ymlfile)
                self.logger.log('info', f"Data read from YAML: {data}")
                return data or {}  # Возвращаем пустой словарь, если data равно None
        except FileNotFoundError:
            self.logger.log('error', "No File Was Found")
            return {}
        except yaml.YAMLError as e:
            self.logger.log('error', f"Error Reading YAML file: {e}")
            return {}
        except Exception as e:
            self.logger.log('error', f"Error: {e}")
            return {}


class Keyboard(Keyboard_path_manager):
    def __init__(self, path=None):
        super().__init__(path)
        self.all_commands = self.parse_yml(self.read_yml())

    def parse_yml(self, yml_data: dict):
        """Парсит YAML-данные и возвращает список команд."""
        commands = yml_data.get("commands", [])
        return [TelebotCommand(command=cmd["command"], description=cmd["description"]) for cmd in commands]

    async def set_menu(self):
        """Устанавливает меню команд в Telegram-боте."""
        if not self.all_commands:
            self.logger.log('error', "No commands found to set menu.")
            return
        commands = [types.BotCommand(command=cmd.command, description=cmd.description) for cmd in self.all_commands]
        await bot.set_my_commands(commands)
        self.logger.log('info', "Menu commands set successfully.")

keyboard = Keyboard()