from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel, Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Jinja
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, SubscribersRefillSG, OrderSG, ServicesData
)

msg = """
➡️ Начало: 0-1 час.
➡️ Скорость: до 45 000 в день
➡️ Списания: случайные (по истечении срока пополнения)
➡️ Пополнение (заправка, гарантия присутствия): 3 дня.
- Пополнение - это гарантия того, что абоненты будут находиться в течение указанного времени на той сумме, на которую сделан их заказ.
- По истечении указанного срока списания могут составлять как 10%, так и 30%, а может и больше процентов.
➡️ Тип пополнения: автоматический.
- Если подписчики исчезнут с канала раньше указанного времени: обязательно свяжитесь с нами, мы их пополним.
➡️ Подходит для чатов, каналов и групп. За исключением анонимных чатов, вход в которые осуществляется только после одобрения администратора.
➡️ Наши подписчики - мы единственные провайдеры

Выберите какие подписчики вам нужны:
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '33751': serv.check_id('33751'),
        '33752': serv.check_id('33752'),
        '33753': serv.check_id('33753'),
        '33754': serv.check_id('33754'),
        '33755': serv.check_id('33755'),
        '33756': serv.check_id('33756'),
        '33757': serv.check_id('33757'),
        '33758': serv.check_id('33758'),
        '33759': serv.check_id('33759'),
    }

sbscrs_refill_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"Русские имена | 3 дня -  ${prices['33751'][1]}/1000"), 
            id='33751', 
            on_click=partial(OrderSG.update, { "id": "33751" }),
            state = OrderSG.order_,
            when=F["33751"]
        ),   
        Start(
            Const(f"Русские имена | 7 дня -  ${prices['33752'][1]}/1000"), 
            id='33752',
            on_click=partial(OrderSG.update, { "id": "33752" }),
            state = OrderSG.order_,
            when=F["33752"]
        ),   
        Start(
            Const(f"Русские имена | 14 дня -  ${prices['33753'][1]}/1000"), 
            id='33753',
            on_click=partial(OrderSG.update, { "id": "33753" }),
            state = OrderSG.order_,
            when=F["33753"]
        ),   
        Start(
            Const(f"Русские имена | 21 дня -  ${prices['33754'][1]}/1000"), 
            id='33754',
            on_click=partial(OrderSG.update, { "id": "33754" }),
            state = OrderSG.order_,
            when=F["33754"]
        ),   
        Start(
            Const(f"Русские имена | 30 дня -  ${prices['33755'][1]}/1000"), 
            id='33755',
            on_click=partial(OrderSG.update, { "id": "33755" }),
            state = OrderSG.order_,
            when=F["33755"]
        ),   
        Start(
            Const(f"Русские имена | 60 дня -  ${prices['33756'][1]}/1000"), 
            id='33756',
            on_click=partial(OrderSG.update, { "id": "33756" }),
            state = OrderSG.order_,
            when=F["33756"]
        ),   
        Start(
            Const(f"Русские имена | 90 дня -  ${prices['33757'][1]}/1000"), 
            id='33757',
            on_click=partial(OrderSG.update, { "id": "33757" }),
            state = OrderSG.order_,
            when=F["33757"]
        ),   
        Start(
            Const(f"Русские имена | 180 дня -  ${prices['33758'][1]}/1000"), 
            id='33758',
            on_click=partial(OrderSG.update, { "id": "33758" }),
            state = OrderSG.order_,
            when=F["33758"]
        ),   
        Start(
            Const(f"Русские имена | 360 дня -  ${prices['33759'][1]}/1000"), 
            id='33759',
            on_click=partial(OrderSG.update, { "id": "33759" }),
            state = OrderSG.order_,
            when=F["33759"]
        ),
        Cancel(Const("Назад")),
        state = SubscribersRefillSG.refill,
        getter=getter
    )
)

