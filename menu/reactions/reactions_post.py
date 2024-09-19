from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, ReactionsPostSG, OrderSG
)

msg = """
➡️ Старт: 0-30 минут
➡️ Скорость: 100К/День
ℹ️ Только публичные ссылки, ко всем реакциям идут просмотры дополнительно
"""

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '31289': serv.check_id('31289'),
        '28515': serv.check_id('28515'),
        '32760': serv.check_id('32760'),
        '28516': serv.check_id('28516'),
        '28517': serv.check_id('28517'),
        '30046': serv.check_id('30046'),
        '30047': serv.check_id('30047'),
        '30050': serv.check_id('30050'),
        '30051': serv.check_id('30051'),
        '30054': serv.check_id('30054'),
        '30062': serv.check_id('30062'),
        '30065': serv.check_id('30065'),
    }

reactions_post_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const("👍🤩🎉🔥❤️"), 
            id='31289', 
            on_click=partial(OrderSG.update, { "id": "31289" }),
            state=OrderSG.order_,
            when=F["31289"]
        ),
        Start(
            Const("👎😁😢💩🤮"), 
            id='28515', 
            on_click=partial(OrderSG.update, { "id": "28515" }),
            state=OrderSG.order_,
            when=F["28515"]
        ),
        Start(
            Const("👍"), 
            id='32760', 
            on_click=partial(OrderSG.update, { "id": "32760" }),
            state=OrderSG.order_,
            when=F["32760"]
        ),
        Start(
            Const("❤️"), 
            id='28516', 
            on_click=partial(OrderSG.update, { "id": "28516" }),
            state=OrderSG.order_,
            when=F["28516"]
        ),
        Start(
            Const("🔥"), 
            id='28517', 
            on_click=partial(OrderSG.update, { "id": "28517" }),
            state=OrderSG.order_,
            when=F["28517"]
        ),
        Start(
            Const("❤️‍🔥"), 
            id='30046', 
            on_click=partial(OrderSG.update, { "id": "30046" }),
            state=OrderSG.order_,
            when=F["30046"]
        ),
        Start(
            Const("🐳"), 
            id='30047', 
            on_click=partial(OrderSG.update, { "id": "30047" }),
            state=OrderSG.order_,
            when=F["30047"]
        ),
        Start(
            Const("🕊️"), 
            id='30050', 
            on_click=partial(OrderSG.update, { "id": "30050" }),
            state=OrderSG.order_,
            when=F["30050"]
        ),
        Start(
            Const("🤡"), 
            id='30051', 
            on_click=partial(OrderSG.update, { "id": "30051" }),
            state=OrderSG.order_,
            when=F["30051"]
        ),
        Start(
            Const("😈"), 
            id='30054', 
            on_click=partial(OrderSG.update, { "id": "30054" }),
            state=OrderSG.order_,
            when=F["30054"]
        ),
        Start(
            Const("💋"), 
            id='30062', 
            on_click=partial(OrderSG.update, { "id": "30062" }),
            state=OrderSG.order_,
            when=F["30062"]
        ),
        Start(
            Const("🍓"), 
            id='30065', 
            on_click=partial(OrderSG.update, { "id": "30065" }),
            state=OrderSG.order_,
            when=F["30065"]
        ),
        Cancel(Const("Назад")),
        state = ReactionsPostSG.reactions_post,
        getter=getter
    )
)
        