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
➡️ Старт: 0-10 минут
➡️ Списания: Нет
➡️​​ Скорость: 50К/День
ℹ️ Только публичные опросы
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '24828': serv.check_id('24828'),
        '33887': serv.check_id('33887'),
    }

sbscr_votes_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"💼Обычные - ${prices['24828'][1]}/1000"),
            id='24828',
            on_click=partial(OrderSG.update, { "id": "24828" }),
            state = OrderSG.order_,
            when=F["24828"]
        ),
        Start(
            Const(f"💼от живых людей - ${prices['33887'][1]}/1000"),
            id='33887',
            on_click=partial(OrderSG.update, { "id": "33887" }),
            state = OrderSG.order_,
            when=F["33887"]
        ),
        Cancel(Const("Назад")),
        state = VotesSG.votes_,
        getter=getter
    )
)

