from asyncio.log import logger
import aiogram
import asyncio
import logging

#============
from aiogram import Bot, Dispatcher, types, F
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram.filters import CommandStart
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog.widgets.kbd import Button, Cancel, Start
from aiogram_dialog.widgets.text import Const
from aiogram.types.error_event import ErrorEvent

from config import Config
from database.db_mysql import MySQLDatabase

from menu.main_ import main_menu
from menu.dev_ import dev_menu
from menu.views.views_ import views_menu
from menu.views.views_future import views_future_menu
from menu.views.views_last import views_last_menu
from menu.views.views_lastorfuture import views_lastorfuture_menu
from menu.views.views_post import views_post_menu
from menu.views.views_shorts import views_shorts_menu
from menu.reactions.reactions_ import reactions_menu
from menu.reactions.reactions_lastorfuture import reactions_lastorfuture_menu
from menu.reactions.reactions_lastorfuturereal import reactions_lastorfuturereal_menu
from menu.reactions.reactions_post import reactions_post_menu
from menu.reactions.reactions_real import reactions_real_menu
from menu.subscribers.subscribers_ import subscribers_menu
from menu.subscribers.subscribers_cheap import sbscr_cheap_menu
from menu.subscribers.subscribers_premium import sbscr_premium_menu
from menu.subscribers.subscribers_stable import sbscr_stable_menu
from menu.subscribers.subscribers_refill import sbscrs_refill_menu
from menu.botsubscribers.botsubscribers_ import sbscr_botsubscribers_menu
from menu.order_history.order_history_ import order_history_menu
from menu.votes.votes_ import sbscr_votes_menu
from menu.shares.shares_ import sbscr_shares_menu
from menu.order.order_ import order_menu
from menu.deposit.deposit_ import debosit_menu
from menu.states import MainSG, AccountDetails, OrderHistorySG, ServicesSG
from api import Api

storage = MemoryStorage()
db = MySQLDatabase()
dp = Dispatcher(storage=storage)

@dp.message(CommandStart())
async def start(message: types.Message, dialog_manager: DialogManager):
    # Вынесем данные из БД по таблице services_local в StatesGroup
    #print(db.GET_services_and_rates())
    #print(ServicesData.services_local)
    await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)

@dp.error()
async def error_handler(event: ErrorEvent, dialog_manager: DialogManager):
    logger.critical("Critical error caused by %s", event.exception, exc_info=True)
    print("error occured")
    await dialog_manager.start(MainSG.main, mode=StartMode.RESET_STACK)

async def main():
    # real main
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=Config().TOKEN)
    dp.include_routers(
        dev_menu,
        views_future_menu,
        views_post_menu,
        views_last_menu,
        views_shorts_menu,
        views_lastorfuture_menu,
        views_menu,
        reactions_menu,
        reactions_lastorfuture_menu,
        reactions_lastorfuturereal_menu,
        reactions_post_menu,
        reactions_real_menu,
        sbscr_premium_menu,
        sbscr_cheap_menu,
        sbscrs_refill_menu,
        sbscr_stable_menu,
        subscribers_menu,
        sbscr_botsubscribers_menu,
        sbscr_votes_menu,
        sbscr_shares_menu,
        order_menu,
        order_history_menu,
        debosit_menu,
        main_menu
    )

    dp.message.register(start, CommandStart())
    setup_dialogs(dp)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())