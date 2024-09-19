from aiogram_dialog import Dialog, StartMode, Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG
)

dev_menu = Dialog(
    Window(
        Const(f"В разработке..."),
        Cancel(Const("Назад")),
        state = DevSG.dev_
    )
)