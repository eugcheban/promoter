from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel, Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Jinja
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, SubscribersPremiumSG, OrderSG, ServicesData
)

msg = """
➡️ Пожалуйста, не делайте заказ одновременно с обычными подписчиками, количество рассчитывается за счет количества участников канала (группы, чата). Сначала заказ на одного должен быть выполнен, а затем заказ перезаказан.

➡️ Начало: 0-3 часа.
➡️ Скорость: 10 тыс./день.
➡️ Списания: Нет
➡️ Премиум-пользователи (активный премиум)
➡️ Делаем это только на публичных аккаунтах
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '32709': serv.check_id('32709'),
        '31525': serv.check_id('31525'),
        '31524': serv.check_id('31524'),
        '33981': serv.check_id('33981'),
        '33982': serv.check_id('33982'),
        '33983': serv.check_id('33983'),
    }

sbscr_premium_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"На 7 дней -  ${prices['32709'][1]}/1000"), 
            id='32709',
            on_click=partial(OrderSG.update, { "id": "33763" }),
            state = OrderSG.order_,
            when=F["32709"]
        ),
        Start(
            Const(f"На 14 дней -  ${prices['31525'][1]}/1000"), 
            id='31525', 
            on_click=partial(OrderSG.update, { "id": "31525" }),
            state = OrderSG.order_,
            when=F["31525"]
        ),
        Start(
            Const(f"на 30 дней -  ${prices['31524'][1]}/1000"), 
            id='31524', 
            on_click=partial(OrderSG.update, { "id": "31524" }),
            state = OrderSG.order_,
            when=F["31524"]
        ),
        Start(
            Const(f"на 45 дней -  ${prices['33981'][1]}/1000"), 
            id='33981', 
            on_click=partial(OrderSG.update, { "id": "33981" }),
            state = OrderSG.order_,
            when=F["33981"]
        ),
        Start(
            Const(f"на 60 дней -  ${prices['33982'][1]}/1000"), 
            id='33982', 
            on_click=partial(OrderSG.update, { "id": "33982" }),
            state = OrderSG.order_,
            when=F["33982"]
        ),
        Start(
            Const(f"на 90 дней -  ${prices['33983'][1]}/1000"), 
            id='33983', 
            on_click=partial(OrderSG.update, { "id": "33983" }),
            state = OrderSG.order_,
            when=F["33983"]
        ),
        Cancel(Const("Назад")),
        state = SubscribersPremiumSG.premium,
        getter = getter
    )
)

