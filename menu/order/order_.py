from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel, Button, SwitchTo, Back
from aiogram_dialog.widgets.text import Const, Jinja
from aiogram_dialog.widgets.input import TextInput
from aiogram.filters.state import State, StatesGroup
from aiogram.types import CallbackQuery
from functools import partial
from magic_filter import F
import re

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, 
    SubscribersStableSG, OrderSG, AccountDetails
)

msg = """
{service_local}

"""
order_info = { 
    "service": None,
    "link": None,
    "quantity": None, 
    "runs": None,
    "intervals": None,
    "comment": None,
    "hashtag": None
}

user_balance = 0
serv = ServicesSG()

async def sw_t_main(event, widget, dialog_manager: DialogManager, *_):
    OrderSG.link = dialog_manager.find("input_link").get_value()
    await dialog_manager.switch_to(OrderSG.order_)

async def getter(dialog_manager: DialogManager, **kwargs):
    accountDetails = AccountDetails(user=kwargs["event_from_user"])
    OrderSG.available_balance = accountDetails.info["balance"]
    OrderSG.order_category = serv.get_service_category(OrderSG.order_id)
    count_window_msg = OrderSG.count_window_msg
    link_window_msg = OrderSG.link_window_msg
    min_order = OrderSG.min_order
    max_order = OrderSG.max_order
    order_id = OrderSG.order_id
    order_rate = OrderSG.order_rate
    order_placement_result = OrderSG.order_placement_result
    user_balance = round(accountDetails.info["balance"], 2)
    link = dialog_manager.find("input_link").get_value()
    count = dialog_manager.find("input_count").get_value()
    order_checks = False

    if order_id == None:
        return

    total_price = ""

    if count == "None":
        count = 0
    if link == "None":
        link = "..."
    

    if isinstance(count, str):
        count = int(count)
    if isinstance(order_rate, str):
        order_rate = float(order_rate)

    total_price = round(float(count) / 1000 * order_rate, 2)
    
    # update OrderSG data
    if link != "...":
        OrderSG.order_id = order_id
        OrderSG.link = link
        OrderSG.quantity = count
        OrderSG.total_price = total_price

    # order checks
    if count >= min_order and link and link != "..." and count < max_order:
        order_checks = True
    else:
        order_checks = False
    
    return {
        "order_name": OrderSG.order_category,
        "link": link,
        "count": count,
        "total_price": total_price,
        "count_window_msg": count_window_msg,
        "link_window_msg": link_window_msg,
        "user_balance": user_balance,
        "min_order": min_order,
        "max_order": max_order,
        "order_placement_result": order_placement_result,
        "order_checks": order_checks
    }

def input_link_filter(message: str) -> bool:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,31}$'
    pattern2 = r'^(?:https?:\/\/t\.me\/)'
    if bool(re.match(pattern, message.text) or re.match(pattern2, message.text)):
        return True
    OrderSG.link_window_msg = f"Ссылка ведена неверно, попробуйте еще раз"
    return False

def input_count_filter(message: str) -> bool:
    try:
        quantity = float(message.text)  # Преобразование введенного текста в целое число
        order_rate = float(OrderSG.order_rate)
        balance = OrderSG.available_balance
        expenses = round(quantity / 1000 * order_rate, 2)  # Вычисление расходов
        if balance < expenses:
            difference = expenses - balance  # Вычисление разницы между расходами и балансом
            OrderSG.count_window_msg = f"Не хватает средств, доступный баланс {balance}, требуется еще {difference}"
            return False
        return True
    except ValueError:
        OrderSG.count_window_msg = f"Количество может содержать только цифры"
        return False

async def place_order(callback: CallbackQuery, button: Button, manager: DialogManager):
    user = callback.from_user
    await OrderSG.place_order(user=user)
    #await OrderSG.reset()

order_menu = Dialog(
    Window(
        Jinja("""
<u>Категория: {{ order_name }} </u>
{% if link != "..." and link %}
✅<b>Ссылка: {{ link }} </b>
{% else %}
⛔️<b>Ссылка: {{ link }} </b>
{% endif %}

{% if count > 0 and count >= min_order and count < max_order %}
✅<b>Количество (мин {{ min_order }}): {{ count }} </b>
{% else %}
⛔️<b>Количество (мин {{ min_order }}): {{ count }} </b>
{% endif %}

<b>Cтоимость / Баланс: {{ total_price }}$ / {{ user_balance }}$</b>
    
        """
        ),
        SwitchTo(
            Const("Указать ссылку"),
            id="switch_linkw",
            state=OrderSG.link_window
        ),
        SwitchTo(
            Const("Указать количество"),
            id='switch_countw',
            state = OrderSG.quantity_window
        ),
        SwitchTo(
            Const("Оформить заказ 🚀"),
            id='order_confirm',
            on_click = place_order,
            state=OrderSG.order_proceed,
            when=F["order_checks"]
        ),
        Cancel(Const("Назад"), on_click=OrderSG.reset),
        getter = getter,
        parse_mode="HTML",
        state = OrderSG.order_
    ),
    # set link
    Window(
        Jinja(" {{ link_window_msg }}"),
        TextInput(
            id="input_link", 
            on_success=sw_t_main,
            filter=input_link_filter
        ),
        SwitchTo(   
            Const("Назад"),
            id="back_from_link",
            state = OrderSG.order_
        ),
        state = OrderSG.link_window,
        getter=getter
    ),
    # set count
    Window(
        Jinja(" {{ count_window_msg }} "),
        TextInput(
            id="input_count", 
            on_success=sw_t_main,
            filter=input_count_filter
        ),
        SwitchTo(
            Const("Назад"),
            id="back_from_count",
            state = OrderSG.order_
        ),
        state = OrderSG.quantity_window,
        getter=getter
    ),
    # order proceeding
    Window(
        Jinja(" {{ order_placement_result }} "),
        SwitchTo(
            Const("Назад"),
            id="back_from_orderproceed",
            state = OrderSG.order_
        ),
        Start(
            Const("В главное меню"),
            id="return_from_orderproceed",
            on_click=OrderSG.reset,
            state = MainSG.main
        ),
        state = OrderSG.order_proceed,
        getter=getter
    )
)
