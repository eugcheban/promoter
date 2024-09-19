from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG,
    ViewsPostSG, ViewsLastorfutureSG, ViewsLastSG, ViewsFutureSG, ViewShortsSG, OrderSG, ServicesData
)

msg = """
Просмотры для истории канала в Telegram
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '31927': serv.check_id('31927'),
        '30066': serv.check_id('30066'),
    }

views_shorts_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"Просмотры в Телеграм - ${prices['31927'][1]}/1000"), 
            id='31927',
            on_click=partial(OrderSG.update, { "id": "31927" }),
            state = OrderSG.order_,
            when=F["31927"]
        ),
        Start(
            Const(f"Просмотры от живых людей - ${prices['30066'][1]}/1000"), 
            id='30066',
            on_click=partial(OrderSG.update, { "id": "30066" }),
            state = OrderSG.order_,
            when=F["30066"]
        ),
        Cancel(Const("Назад")),
        state = ViewShortsSG.views_shorts,
        getter=getter
    )
)