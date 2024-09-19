from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Url
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.api.entities import MediaAttachment, MediaId
from aiogram_dialog.widgets.media import DynamicMedia, StaticMedia
from aiogram.enums import ContentType
from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, OrderHistorySG, DepositSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, AccountDetails
)
from database.db_mysql import MySQLDatabase
from config import Config

db = MySQLDatabase()
config = Config()

async def getter(**kwargs):
    accountDetails = AccountDetails(user=kwargs['event_from_user'])
    if accountDetails.info:
        user_name = accountDetails.info.get('user_name')
        balance = accountDetails.info.get('balance')
        if user_name is not None and balance is not None:
            print(f"{user_name} has a balance of ${balance}")
        else:
            print("User information is incomplete")

        return {
            "user_name": user_name,
            "balance": round(balance, 2)
        }
    else:
        print("User information not found")
    
    return None

main_menu = Dialog(
    Window(
        StaticMedia(
            path="./menu/logo2.png",
            type=ContentType.PHOTO,
        ),
        Format("Добро пожаловать в ZazAtack @{user_name}, ваш личный помощник продвижения в Telegram! \n\nВаш текущий баланс: ${balance} \n\n 👥Подписчики от 3$ за 1к \n 👀Просмотры от 0.14$ за 1к"),
        Start(
            Const("👥 Подписчики"), 
            id="subscribers_", 
            state=SubscribersSG.subscribers_
        ),
        Start(
            Const("👀 Просмотры"), 
            id="views_", 
            state=ViewsSG.views_
        ),
        Start(
            Const("😎 Реакции"), 
            id="reactions_", 
            state=ReactionsSG.reactions_
        ),
        Start(
            Const("🤖Подписчики для Telegram-бота"), 
            id='telegrambotsmembers', 
            state=BotsActivationSG.bots_
        ),
        Start(
            Const("💼Голоса для опросов"), 
            id='votes_', 
            state=VotesSG.votes_
        ),
        Start(
            Const("🔄Репосты постов"), 
            id='shares_', 
            state=SharesSG.shares_
        ),
        Start(
            Const("📓 Мои заказы"), 
            id='order_history_',
            state=OrderHistorySG.order_history_
        ),
        Start(
            Const("💰 Пополнить баланс"), 
            id='deposit_',
            state=DepositSG.deposit_
        ),
        Url(
            Const("Поддержка"), 
            Const(config.admin), 
        ),
        state = MainSG.main,
        getter = getter
    )
)