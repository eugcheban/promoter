from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel, Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Jinja
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, SubscribersStableSG, OrderSG, ServicesData
)

msg = """
➡️ Старт: 0-30 минут
➡️ Скорость: 5500 в день
➡️ Ссылка: ссылка на Telegram-бота
➡️ Это обычные запуски для Telegram-бота (так если: активация функции запуска). Это не подписчики. Мы просто активируем вашего бота за своими аккаунтами.
➡️ Они не станут рефералами - не используйте на реферальные ссылки, так как они не принесут вам пользы.

Выберите какие подписчики вам нужны:
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '32711': serv.check_id('32711'),
        '32710': serv.check_id('32710'),
        '33173': serv.check_id('33173'),
    }

sbscr_botsubscribers_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"Запуски бота - ${prices['32711'][1]}/1000"),
            id='32711',
            on_click=partial(OrderSG.update, { "id": "32711" }),
            state = OrderSG.order_,
            when=F["32711"]
        ),
        Start(
            Const(f"Премиум запуски бота - ${prices['32710'][1]}/1000"),
            id='32710',
            on_click=partial(OrderSG.update, { "id": "32710" }),
            state = OrderSG.order_,
            when=F["32710"]
        ),
        Start(
            Const(f"Живые люди для бота - ${prices['33173'][1]}/1000"),
            id='33173',
            on_click=partial(OrderSG.update, { "id": "33173" }),
            state = OrderSG.order_,
            when=F["33173"]
        ),
        Cancel(Const("Назад")),
        state = BotsActivationSG.bots_,
        getter=getter
    )
)

