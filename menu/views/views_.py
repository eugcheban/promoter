from aiogram_dialog import Dialog, StartMode, Window
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG,
    ReactionsSG, VotesSG, SharesSG, MainSG,
    ViewsPostSG, ViewsLastorfutureSG, ViewsLastSG, ViewsFutureSG, ViewShortsSG
)

msg = """
Накрутка просмотров в телеграм - способ продвижения который дает активность вашему каналу.
"""
views_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const("👀Просмотры на пост"), 
            id='views_',
            state=ViewsPostSG.views_post
        ),   
        Start(
            Const("👀 на последние или будущие посты"), 
            id='views_lastorfuture', 
            state=ViewsLastorfutureSG.views_lastorfuture
        ),   
        Start(
            Const("👀 для последних постов"), 
            id='views_las', 
            state=ViewsLastSG.views_last
        ),   
        Start(
            Const("👀 для будущих постов"), 
            id='views_future', 
            state=ViewsFutureSG.views_future
        ),   
        Start(
            Const("👀 для истории"), 
            id='views_shorts', 
            state=ViewShortsSG.views_shorts
        ), 
        Cancel(Const("Назад")),
        state = ViewsSG.views_
    )
)