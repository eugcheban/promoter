from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel
from aiogram_dialog.widgets.text import Const
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ReactionsLastorfuturerealSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, ReactionsLastorfutureSG, OrderSG
)

msg = """
➡️ Почему нет цены: цена рассчитывается при создании каждого заказа (1 заказ = 1 пост) - у вас должны быть деньги на балансе, иначе заказ будет в статусе паузы.

➡️ Как заказать:
1) Имя пользователя: ссылка или имя канала через @ (осторожно с пробелами, их не должно быть справа и слева - форма чувствительна к заполнению)
2) Новые посты: количество будущих постов, на которые требуются реакции (если не надо - поставьте 0)
3) Старые посты: количество уже опубликованных постов, на которые требуются реакции (если не надо - поставьте 0)
4) Количество: количество реакций на каждый пост (100 и 100 = 100 реакций, если укажите 100 и 250 = любое число от 100 до 250)
5) Задержка: установите значение 10 или 15 - это оптимальные значения.
6) Конечная дата: поле не обязательно для заполнения

***

➡️ Старт: 0-30 минут
➡️ Скорость: 100К/День
"""

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '33760': serv.check_id('33760'),
        '33761': serv.check_id('33761'),
        '33762': serv.check_id('33762'),
        '33763': serv.check_id('33763'),
        '33764': serv.check_id('33764'),
        '33765': serv.check_id('33765'),
        '33766': serv.check_id('33766'),
        '33767': serv.check_id('33767'),
        '33768': serv.check_id('33768'),
        '33769': serv.check_id('33769'),
        '33770': serv.check_id('33770'),
        '33771': serv.check_id('33771'),
        '33772': serv.check_id('33772'),
        '33773': serv.check_id('33773'),
        '33774': serv.check_id('33774'),
        '33775': serv.check_id('33775'),
        '33776': serv.check_id('33776'),
    }

reactions_lastorfuture_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const("👍🤩🎉🔥❤️"), 
            id='33765',
            on_click=partial(OrderSG.update, { "id": "33765" }), 
            state=OrderSG.order_,
            when=F["33765"]
        ),
        Start(
            Const("👎😁😢💩🤮"), 
            id='33766',
            on_click=partial(OrderSG.update, { "id": "33766" }), 
            state=OrderSG.order_,
            when=F["33766"]
        ),
        Start(
            Const("👍"), 
            id='33767', 
            on_click=partial(OrderSG.update, { "id": "33767" }),
            state=OrderSG.order_,
            when=F["33767"]
        ),
        Start(
            Const("❤️"), 
            id='33768', 
            on_click=partial(OrderSG.update, { "id": "33768" }),
            state=OrderSG.order_,
            when=F["33768"]
        ),
        Start(
            Const("🔥"), 
            id='33769', 
            on_click=partial(OrderSG.update, { "id": "33769" }),
            state=OrderSG.order_,
            when=F["33769"]
        ),
        Start(
            Const("❤️‍🔥"), 
            id='33770', 
            on_click=partial(OrderSG.update, { "id": "33770" }),
            state=OrderSG.order_,
            when=F["33770"]
        ),
        Start(
            Const("🐳"), 
            id='33771', 
            on_click=partial(OrderSG.update, { "id": "33771" }),
            state=OrderSG.order_,
            when=F["33771"]
        ),
        Start(
            Const("🕊️"), 
            id='33772', 
            on_click=partial(OrderSG.update, { "id": "33772" }),
            state=OrderSG.order_,
            when=F["33772"]
        ),
        Start(
            Const("🤡"), 
            id='33773', 
            on_click=partial(OrderSG.update, { "id": "33773" }),
            state=OrderSG.order_,
            when=F["33773"]
        ),
        Start(
            Const("😈"), 
            id='33774', 
            on_click=partial(OrderSG.update, { "id": "33774" }),
            state=OrderSG.order_,
            when=F["33774"]
        ),
        Start(
            Const("💋"), 
            id='33775', 
            on_click=partial(OrderSG.update, { "id": "33775" }),
            state=OrderSG.order_,
            when=F["33775"]
        ),
        Start(
            Const("🍓"), 
            id='33776', 
            on_click=partial(OrderSG.update, { "id": "33776" }),
            state=OrderSG.order_,
            when=F["33776"]
        ),
        Cancel(Const("Назад")),
        state = ReactionsLastorfutureSG.reactions_lastorfuture,
        getter=getter
    )
)
             