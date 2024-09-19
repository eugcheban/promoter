from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Jinja
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, SubscribersCheapSG, 
    SubscribersStableSG, SubscribersRefillSG, SubscribersPremiumSG
)

msg = """
*Накрутка подписчиков Телеграм*
_Стабильные_ - почти без отписок, до 10%
_Возобновляемые_ - отписки возобновляются, гарантия
_Дешовые_ - гарантий на отписки нет

"""
serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return { 
        "pdp_refill": serv.check_id('0239'), #test = false
        "29492": serv.check_id('29492'),
        "subscribers_cheap": False,
        "subscribers_premium": True,
    }

subscribers_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const("👥Подписчики | Стабильные"), 
            id='subscribers_stable_29492', 
            state=SubscribersStableSG.stable,
            when=F["29492"]
        ),   
        Start(
            Const("👥Подписчики | Возобновляемые"), 
            id='subscribers_refill', 
            state=SubscribersRefillSG.refill,
            when=F["pdp_refill"]
        ),   
        Start(
            Const("👥Подписчики | Дешовые"), 
            id='subscribers_cheap', 
            state=SubscribersCheapSG.cheap,
            when=F["subscribers_cheap"]
        ),
        Start(
            Const("👥Подписчики | Премиум"), 
            id='subscribers_premium', 
            state=SubscribersPremiumSG.premium,
            when=F["subscribers_premium"]
        ),
        Cancel(Const("Назад")),
        state = SubscribersSG.subscribers_,
        getter=getter
    ),
)

