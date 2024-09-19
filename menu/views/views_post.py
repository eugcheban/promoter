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
➡️ Старт: 0-1 час
- Иногда может быть нестабильным, вплоть до 12 часов
➡️ Скорость: до 1 550 000 в день на 1 ссылку
ℹ️ Только публичные ссылки
ℹ️ Ответ на частый запрос: а что делать, если не будет выполнено? Ведь тариф указан как не стабильный - это наши сервисы, через время, если не будет готово (1 день, как правило), мы осуществим выполнение услуги своими силами (писать нет необходимости). Такое происходит очень редко.
"""

prices = ServicesData.services_local

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '32855': serv.check_id('32855'),
        '32752': serv.check_id('32752'),
        '33285': serv.check_id('33285'),
        '31931': serv.check_id('31931'),
        '33497': serv.check_id('33497'),
    }

views_post_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"Медленные - ${prices['32855'][1]}/1000"), 
            id='32855', 
            on_click=partial(OrderSG.update, { "id": "32855" }),
            state = OrderSG.order_,
            when=F["32855"]
        ),
        Start(
            Const(f"Очень быстрые + реакции - ${prices['32752'][1]}/1000"), 
            id='32752', 
            on_click=partial(OrderSG.update, { "id": "32752" }),
            state = OrderSG.order_,
            when=F["32752"]
        ),
        Start(
            Const(f"Ультра быстрые + реакции - ${prices['33285'][1]}/1000"), 
            id='33285', 
            on_click=partial(OrderSG.update, { "id": "33285" }),
            state = OrderSG.order_,
            when=F["33285"]
        ),
        Start(
            Const(f"От Premium пользователей - ${prices['31931'][1]}/1000"), 
            id='31931', 
            on_click=partial(OrderSG.update, { "id": "31931" }),
            state = OrderSG.order_,
            when=F["31931"]
        ),
        Start(
            Const(f"Для тематик 18+ - ${prices['33497'][1]}/1000"), 
            id='33497', 
            on_click=partial(OrderSG.update, { "id": "33497" }),
            state = OrderSG.order_,
            when=F["33497"]
        ),
        Cancel(Const("Назад")),
        state = ViewsPostSG.views_post,
        getter=getter
    )
)
