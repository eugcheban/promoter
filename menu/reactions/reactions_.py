from aiogram_dialog import Dialog, StartMode, Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ReactionsLastorfuturerealSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, ReactionsRealSG, ReactionsLastorfutureSG, ReactionsPostSG
)

msg = """
Накрутка реакций - позитивные/негативные
"""
reactions_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const("😎на пост"), 
            id='reactions_', 
            state=ReactionsPostSG.reactions_post
        ),   
        Start(
            Const("😎для последних или будущих постов"), 
            id='reactions_lastorfuture', 
            state=ReactionsLastorfutureSG.reactions_lastorfuture
        ),   
        Start(
            Const("😎от реальных людей"), 
            id='reactions_real', 
            state=ReactionsRealSG.reactions_real
        ),   
        Start(
            Const("😎для посл. или буд. от реальных"), 
            id='reactions_lastorfuturereal', 
            state=ReactionsLastorfuturerealSG.reactions_lastorfuturereal
        ),
        Cancel(Const("Назад")),
        state = ReactionsSG.reactions_
    )
)
        