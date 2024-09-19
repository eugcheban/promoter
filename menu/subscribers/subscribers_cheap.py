from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel, Button
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.text import Jinja
from functools import partial
from magic_filter import F

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, SubscribersCheapSG, ServicesData, OrderSG
)

msg = """
➡️ ВНИМАНИЕ: УСЛУГА ПРЕДОСТАВЛЯЕТСЯ БЕЗ ГАРАНТИИ. СПИСАНИЕ МОЖЕТ ПРОИЗОЙТИ СРАЗУ, В ДЕНЬ ЗАКАЗА ИЛИ ПОСЛЕ ВРЕМЕНИ. НИКАКИХ ГАРАНТИЙ. УСКОРЕНИЕ НЕ ГАРАНТИРУЕТСЯ. ВЫ ЗАКАЗЫВАЕТЕ УСЛУГУ НА СВОЙ РИСК.
➡️ ПРОЧИТАЙТЕ ОПИСАНИЕ. ПОМНИТЕ, МЫ ЧЕСТНЫ С ВАМИ - МЫ ПРЕДУПРЕЖДАЛИ ОБ ВСЕМ ЗАРАНЕЕ, ЧТОБЫ НЕ БЫЛО НЕПОНЯТИЙ И ВОПРОСОВ В БУДУЩЕМ.
➡️ ЭТО МУСОРНЫЕ ПРОФИЛИ. МУСОР ЕСТЬ МУСОР. ОНИ НИЗКОГО КАЧЕСТВА, ПОЭТОМУ НИКАКИХ ГАРАНТИЙ НЕТ И НЕ БУДЕТ. ВОЗВРАТА ИЛИ ОТМЕНЫ ЗАКАЗОВ НЕТ.

➡️ Начало: 0-1 час.
- Старт может быть выше (до 3 дней)
- Заказ нельзя отменить (максимум - ускориться, но ускорение не гарантировано)
- Если старт не займет много времени - свяжитесь с нами
➡️ Скорость: около 10 000 в день.
- Может быть, это выше
- Может быть, ниже
➡️ Максимум 60 000 (это лимит на 1 канал, группу или чат)
➡️ Гарантия: нет, нет и еще раз нет.
- Никакая гарантия не предоставляется ни в какой форме.
- Вы пользуетесь услугой на свой страх и риск
- Списания не являются аргументом для отмены заказа и возврата денег.
➡️ Списания: до 100%
- Списание может произойти немедленно.
- Списание может произойти в течение суток
- Списания могут быть небольшими. средний или высокий
- Списание может быть полным.
➡️ Мы принимаем только публичные ссылки.
- Не присылайте ссылки на анонимные чаты и группы
--- Такие заказы принимаются без возврата и отмены.
--- Вы соглашаетесь с этим условием.

Выберите какие подписчики вам нужны: (полное описание по переходу)
"""

prices = ServicesData.services_local

async def get_data_for_next_dialog(**kwargs):
    return {"key": "value"}

serv = ServicesSG()

async def getter(dialog_manager: DialogManager, **kwargs):
    return {
        '33760': serv.check_id('33760'),
        '33761': serv.check_id('33761'),
        '33762': serv.check_id('33762'),
        '33763': serv.check_id('33763'),
    }

sbscr_cheap_menu = Dialog(
    Window(
        Const(msg),
        Start(
            Const(f"Вариант №1 -  ${prices['33760'][1]}/1000"),
            id='33760',
            on_click=partial(OrderSG.update, { "id": "33760" }),
            state = OrderSG.order_,
            when=F["33760"]
        ),
        Start(
            Const(f"Вариант №2 -  ${prices['33761'][1]}/1000"),
            id='33761', 
            on_click=partial(OrderSG.update, { "id": "33761" }),
            state = OrderSG.order_,
            when=F["33761"]
        ),
        Start(
            Const(f"Вариант №3 -  ${prices['33762'][1]}/1000"), 
            id='33762', 
            on_click=partial(OrderSG.update, { "id": "33762" }),
            state = OrderSG.order_,
            when=F["33762"]
        ),
        Start(
            Const(f"Вариант №4 -  ${prices['33763'][1]}/1000"), 
            id='33763', 
            on_click=partial(OrderSG.update, { "id": "33763" }),
            state = OrderSG.order_,
            when=F["33763"]
        ),
        Cancel(Const("Назад")),
        state = SubscribersCheapSG.cheap,
        getter = getter
    )
)

