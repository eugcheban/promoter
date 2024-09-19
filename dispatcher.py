from aiogram import Dispatcher
from aiogram_dialog import DialogManager
from aiogram.fsm.storage.memory import MemoryStorage


storage = MemoryStorage()
# Создаем экземпляр диспетчера
dp = Dispatcher(storage=storage)

# Создаем экземпляр менеджера диалогов
dialog_manager = DialogManager(dp)
