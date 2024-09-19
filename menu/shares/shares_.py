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
➡️​​ Скорость: 5К/День
ℹ️ Поддержка: Channel Analytics, Telemetr и Tgstat
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return { 
        '24839': serv.check_id('24839'),
        '30067': serv.check_id('30067'),
        '31376': serv.check_id('31376'),
    }

sbscr_shares_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"🔄Обычные - ${prices['24839'][1]}/1000"),
            id='24839',
            on_click=partial(OrderSG.update, { "id": "24839" }),
            state = OrderSG.order_,
            when=F["24839"]
        ),
        Start(
            Const(f"🔄 + просмотры - ${prices['30067'][1]}/1000"),
            id='30067',
            on_click=partial(OrderSG.update, { "id": "30067" }),
            state = OrderSG.order_,
            when=F["30067"]
        ),
        Start(
            Const(f"🔄 + 👀 - живых людей - ${prices['31376'][1]}/1000"),
            id='31376',
            on_click=partial(OrderSG.update, { "id": "31376" }),
            state = OrderSG.order_,
            when=F["31376"]
        ),
        Cancel(Const("Назад")),
        state = SharesSG.shares_,
        getter=getter
    )
)

