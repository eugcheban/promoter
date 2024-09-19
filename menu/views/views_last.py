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
➡️ Старт: 0-4 часа
➡️ Скорость: 5М/День
➡️ Особая характеристика: просмотры на 5 последних постов (заказали 1000 - придет 1000 на каждый из 5 последних постов)
ℹ️ Ваш канал/чат/группа должны быть публичными и в течении последних 14 дней не находится в приватном статусе.
ℹ️ Автоматический переход в статус "выполнен" после заказа. Выполнение осуществляется в течение 12 часов после заказа.
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '30016': serv.check_id('30016'),
        '30017': serv.check_id('30017'),
        '30018': serv.check_id('30018'),
        '30019': serv.check_id('30019'),
        '30020': serv.check_id('30020'),
        '30021': serv.check_id('30021'),
        '33019': serv.check_id('33019'),
        '33020': serv.check_id('33020'),
        '30022': serv.check_id('30022'),
        '30023': serv.check_id('30023'),
        '33010': serv.check_id('33010'),
        '33011': serv.check_id('33011'),
    }

views_last_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"5 постов - ${prices['30016'][1]}/1000"), 
            id='30016', 
            on_click=partial(OrderSG.update, { "id": "30016" }),
            state=OrderSG.order_,
            when=F["30016"]
        ),
        Start(
            Const(f"10 постов - ${prices['30017'][1]}/1000"), 
            id='30017', 
            on_click=partial(OrderSG.update, { "id": "30017" }),
            state=OrderSG.order_,
            when=F["30017"]
        ),
        Start(
            Const(f"20 постов - ${prices['30018'][1]}/1000"), 
            id='30018', 
            on_click=partial(OrderSG.update, { "id": "30018" }),
            state=OrderSG.order_,
            when=F["30018"]
        ),
        Start(
            Const(f"50 постов - ${prices['30019'][1]}/1000"), 
            id='30019', 
            on_click=partial(OrderSG.update, { "id": "30019" }),
            state=OrderSG.order_,
            when=F["30019"]
        ),
        Start(
            Const(f"100 постов - ${prices['30020'][1]}/1000"), 
            id='30020', 
            on_click=partial(OrderSG.update, { "id": "30020" }),
            state=OrderSG.order_,
            when=F["30020"]
        ),
        Start(
            Const(f"200 постов - ${prices['30021'][1]}/1000"), 
            id='30021', 
            on_click=partial(OrderSG.update, { "id": "30021" }),
            state=OrderSG.order_,
            when=F["30021"]
        ),
        Start(
            Const(f"300 постов - ${prices['33019'][1]}/1000"), 
            id='33019', 
            on_click=partial(OrderSG.update, { "id": "33019" }),
            state=OrderSG.order_,
            when=F["33019"]
        ),
        Start(
            Const(f"400 постов - ${prices['33020'][1]}/1000"), 
            id='33020', 
            on_click=partial(OrderSG.update, { "id": "33020" }),
            state=OrderSG.order_,
            when=F["33020"]
        ),
        Start(
            Const(f"500 постов - ${prices['30022'][1]}/1000"), 
            id='30022', 
            on_click=partial(OrderSG.update, { "id": "30022" }),
            state=OrderSG.order_,
            when=F["30022"]
        ),
        Start(
            Const(f"750 постов - ${prices['30023'][1]}/1000"), 
            id='30023', 
            on_click=partial(OrderSG.update, { "id": "30023" }),
            state=OrderSG.order_,
            when=F["30023"]
        ),
        Start(
            Const(f"1000 постов - ${prices['33010'][1]}/1000"), 
            id='33010', 
            on_click=partial(OrderSG.update, { "id": "33010" }),
            state=OrderSG.order_,
            when=F["33010"]
        ),
        Start(
            Const(f"1500 постов - ${prices['33011'][1]}/1000"), 
            id='33011', 
            on_click=partial(OrderSG.update, { "id": "33011" }),
            state=OrderSG.order_,
            when=F["33011"]
        ),
        Cancel(Const("Назад")),
        state = ViewsLastSG.views_last,
        getter=getter
    )
)