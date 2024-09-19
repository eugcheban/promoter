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
Также советуем заказывать подписчиков с Премиумом в пропорции 5% от заказанного количества постоянных подписчиков. Это улучшит видимость канала/группы в результатах поиска и минимизирует риск попадания канала/группы в список «использует ботов».

➡️ ПРИНИМАЕМ ТОЛЬКО КАНАЛЫ С РЕГИСТРАЦИЕЙ ОТ 3-Х ДНЕЙ

➡️ Начало: 0-10 минут.
➡️ Скорость: 45 тыс./день.
➡️ Списания: Нет или минимальны.

Выберите какие подписчики вам нужны:
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '30830': serv.check_id('30830'),
        '33345': serv.check_id('33345'),
        '33750': serv.check_id('33750'),
        '31436': serv.check_id('31436'),
        '24728': serv.check_id('24728'),
    }

sbscr_stable_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"Русские имена ${prices['30830'][1]}/1000"), 
            id='30830',
            on_click=partial(OrderSG.update, { "id": "30830" }),
            state = OrderSG.order_,
            when=F["30830"]
        ),   
        Start(
            Const(f"Русские имена ${prices['33345'][1]}/1000"), 
            id='33345',
            on_click=partial(OrderSG.update, { "id": "33345" }),
            state = OrderSG.order_,
            when=F["33345"]
        ),   
        Start(
            Const(f"Английские имена ${prices['33750'][1]}/1000"), 
            id='33750',
            on_click=partial(OrderSG.update, { "id": "33750" }),
            state = OrderSG.order_,
            when=F["33750"]
        ),   
        Start(
            Const(f"Английские имена ${prices['31436'][1]}/1000"), 
            id='31436',
            on_click=partial(OrderSG.update, { "id": "31436" }),
            state = OrderSG.order_,
            when=F["31436"]
        ),   
        Start(
            Const(f"Смешанные имена ${prices['31438'][1]}/1000"), 
            id='31438',
            on_click=partial(OrderSG.update, { "id": "31438" }),
            state = OrderSG.order_,
            when=F["31438"]
        ),   
        Start(
            Const(f"Реальные люди ${prices['24728'][1]}/1000"), 
            id='24728',
            on_click=partial(OrderSG.update, { "id": "24728" }),
            state = OrderSG.order_,
            when=F["24728"]
        ), 
        Cancel(Const("Назад")),
        state = SubscribersStableSG.stable,
        getter=getter
    )
)

