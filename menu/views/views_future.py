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
➡️ Почему нет цены: цена рассчитывается при создании каждого заказа (1 заказ = 1 пост) - у вас должны быть деньги на балансе, иначе заказ будет в статусе паузы.

➡️ Как заказать:
1) Имя пользователя: ссылка или имя канала через @ (осторожно с пробелами, их не должно быть справа и слева - форма чувствительна к заполнению)
2) Новые посты: количество будущих постов, на которые требуются просмотры (если не надо - поставьте 0)
3) Старые посты: количество уже опубликованных постов, на которые требуются просмотры (если не надо - поставьте 0)
4) Количество: количество просмотров на каждый пост (100 и 100 = 100 просмотров, если укажите 100 и 250 = любое число от 100 до 250)
5) Задержка: установите значение 10 или 15 - это оптимальные значения.
6) Конечная дата: поле не обязательно для заполнения
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '31933': serv.check_id('31933'),
        '33167': serv.check_id('33167'),
        '33281': serv.check_id('33281'),
    }

views_future_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"5 постов - ${prices['31933'][1]}/1000"), 
            id='31933', 
            on_click=partial(OrderSG.update, { "id": "31933" }),
            state = OrderSG.order_,
            when=F["31933"]
        ),
        Start(
            Const(f"10 постов - ${prices['33167'][1]}/1000"), 
            id='33167', 
            on_click=partial(OrderSG.update, { "id": "33167" }),
            state = OrderSG.order_,
            when=F["33167"]
        ),
        Start(
            Const(f"15 постов - ${prices['33281'][1]}/1000"), 
            id='33281', 
            on_click=partial(OrderSG.update, { "id": "33281" }),
            state = OrderSG.order_,
            when=F["33281"]
        ),
        Cancel(Const("Назад")),
        state = ViewsFutureSG.views_future,
        getter=getter
    )
)