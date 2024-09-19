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
        '33496': serv.check_id('33496'),
        '33330': serv.check_id('33330'),
        '33331': serv.check_id('33331'),
        '33332': serv.check_id('33332'),
        '33333': serv.check_id('33333'),
        '33498': serv.check_id('33498'),
    }

views_lastorfuture_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"Нестабильные - ${prices['33496'][1]}/1000"), 
            id='33496', 
            on_click=partial(OrderSG.update, { "id": "33496" }),
            state=OrderSG.order_,
            when=F["33496"]
        ),
        Start(
            Const(f"Медленные - ${prices['33330'][1]}/1000"), 
            id='33330', 
            on_click=partial(OrderSG.update, { "id": "33330" }),
            state=OrderSG.order_,
            when=F["33330"]
        ),
        Start(
            Const(f"Очень быстрые + реакции - ${prices['33331'][1]}/1000"), 
            id='33331', 
            on_click=partial(OrderSG.update, { "id": "33331" }),
            state=OrderSG.order_,
            when=F["33331"]
        ),
        Start(
            Const(f"Ультра быстрые + реакции - ${prices['33332'][1]}/1000"), 
            id='33332', 
            on_click=partial(OrderSG.update, { "id": "33332" }),
            state=OrderSG.order_,
            when=F["33332"]
        ),
        Start(
            Const(f"От Premium пользователей - ${prices['33333'][1]}/1000"), 
            id='33333', 
            on_click=partial(OrderSG.update, { "id": "33333" }),
            state=OrderSG.order_,
            when=F["33333"]
        ),
        Start(
            Const(f"Для тематик 18+ - ${prices['33498'][1]}/1000"), 
            id='33498', 
            on_click=partial(OrderSG.update, { "id": "33498" }),
            state=OrderSG.order_,
            when=F["33498"]
        ),
        Cancel(Const("Назад")),
        state = ViewsLastorfutureSG.views_lastorfuture,
        getter=getter
    )
)