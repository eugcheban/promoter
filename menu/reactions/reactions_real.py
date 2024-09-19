from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, ReactionsRealSG, OrderSG
)

msg = """
➡️ Старт: 0-2 часа
➡️ Скорость: 10К/День
ℹ️ Только публичные ссылки
ℹ️ Для выполнения данной работы используются действующие арендованные аккаунты реальных людей.
ℹ️ Заказывая на тематики, которые связаны с войной, конфликтами, разжиганием розни между конфессиями и народами, порнографией, наркотическими веществами, и иными схожими с ними по смыслу вы рискуете получить недокрут частичный или полный, отмену без возврата денежных средств.
"""

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '30442': serv.check_id('31289'),
        '30443': serv.check_id('28515'),
        '30444': serv.check_id('32760'),
        '30445': serv.check_id('28516'),
        '30446': serv.check_id('28517'),
        '30447': serv.check_id('30046'),
        '30448': serv.check_id('30047'),
        '30449': serv.check_id('30050'),
        '30450': serv.check_id('30051'),
        '30451': serv.check_id('30054'),
        '30452': serv.check_id('30062'),
        '30453': serv.check_id('30065'),
    }

reactions_real_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const("👍🤩🎉🔥❤️"), 
            id='30442',
            on_click=partial(OrderSG.update, { "id": "30442" }),
            state=OrderSG.order_,
            when=F["30442"]
        ),
        Start(
            Const("👎😁😢💩🤮"), 
            id='30443',
            on_click=partial(OrderSG.update, { "id": "30443" }),
            state=OrderSG.order_,
            when=F["30443"]
        ),
        Start(
            Const("👍"), 
            id='30444',
            on_click=partial(OrderSG.update, { "id": "30444" }),
            state=OrderSG.order_,
            when=F["30444"]
        ),
        Start(
            Const("👎"), 
            id='30445',
            on_click=partial(OrderSG.update, { "id": "30445" }),
            state=OrderSG.order_,
            when=F["30445"]
        ),
        Start(
            Const("🔥"), 
            id='30446',
            on_click=partial(OrderSG.update, { "id": "30446" }),
            state=OrderSG.order_,
            when=F["30446"]
        ),
        Start(
            Const("❤️"), 
            id='30447',
            on_click=partial(OrderSG.update, { "id": "30447" }),
            state=OrderSG.order_,
            when=F["30447"]
        ),
        Start(
            Const("🎉"), 
            id='30448',
            on_click=partial(OrderSG.update, { "id": "30448" }),
            state=OrderSG.order_,
            when=F["30448"]
        ),
        Start(
            Const("🤩"), 
            id='30449',
            on_click=partial(OrderSG.update, { "id": "30449" }),
            state=OrderSG.order_,
            when=F["30449"]
        ),
        Start(
            Const("💩"), 
            id='30450',
            on_click=partial(OrderSG.update, { "id": "30450" }),
            state=OrderSG.order_,
            when=F["30450"]
        ),
        Start(
            Const("🤮"), 
            id='30451',
            on_click=partial(OrderSG.update, { "id": "30451" }),
            state=OrderSG.order_,
            when=F["30451"]
        ),
        Start(
            Const("😁"), 
            id='30452',
            on_click=partial(OrderSG.update, { "id": "30452" }),
            state=OrderSG.order_,
            when=F["30452"]
        ),
        Start(
            Const("😢"), 
            id='30453',
            on_click=partial(OrderSG.update, { "id": "30453" }),
            state=OrderSG.order_,
            when=F["30453"]
        ),
        Start(
            Const("😱"), 
            id='30454',
            on_click=partial(OrderSG.update, { "id": "30454" }),
            state=OrderSG.order_,
            when=F["30454"]
        ),
        Cancel(Const("Назад")),
        state = ReactionsRealSG.reactions_real,
        getter=getter
    )
)