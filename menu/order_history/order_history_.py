from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel, Button, SwitchTo, Row
from aiogram_dialog.widgets.input import TextInput, ManagedTextInput
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Jinja
from functools import partial
import asyncio
from aiogram.types import CallbackQuery, Message
from database.db_mysql import MySQLDatabase
from api import Api

from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, OrderHistorySG, AccountDetails, BufferSG,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, SubscribersStableSG, OrderSG, ServicesData
)

db = MySQLDatabase()
ap = Api()

msg = """
➡️ Старт: 0-10 минут
➡️ Списания: Нет
➡️​​ Скорость: 50К/День
ℹ️ Только публичные опросы
"""

async def on_start(*args, **kwargs):
    BufferSG.cancel_response = None

async def getter(dialog_manager: DialogManager, **kwargs):
    accountDetails = AccountDetails(user=kwargs['event_from_user'])
    #accountDetails.info["order_history"] = []
    await accountDetails.update()
    data = accountDetails.info["order_history"]
    return {
        "data": data,
        "orders": len(data),
        "cancel_response": BufferSG.cancel_response
    }

async def input_orderid_filter(message: str) -> bool:
    msg = message.html_text
    print(message.html_text)
    order_id = 0
    command = None
    if '_' in msg:
        command = msg.split('_')[0]
        order_id = msg.split('_')[1]
        # check the correction index of order
        if len(order_id) <= 0:
            db.SET_log_record(f"Wrong ID command! {msg}")
            return False
    else:
        db.SET_log_record(f"Wrong command! {msg}")
        return False
    return True

async def order_cancel(callback: CallbackQuery, widget: ManagedTextInput[str], manager: DialogManager, data: str):
    order_id = data.split('_')[1]
    try:
        response = ap.cancel(order_id)
        print(response)

        # Проверяем, есть ли ключ 'error' в ответе
        if 'error' in response:
            # Проверяем значение ошибки
            if response['error'] == 'error.cancel_unavailable':
                db.SET_log_record(f"Error: {response['error']}")
                BufferSG.cancel_response = "Не удалось закрыть заказ."
            else:
                # Обработка других типов ошибок
                db.SET_log_record(f"Error: {response['error']}")
                BufferSG.cancel_response = "Произошла ошибка при закрытии заказа."
        else:
            # Если ошибки нет, запрос выполнен успешно
            # Обработка успешного выполнения запроса
            print("Заказ успешно закрыт")
            # оповестить админа про закрытие заказа, вручную вернуть средства на счет пользователя
            db.SET_log_record(f"Order # {order_id} had been canceled")

    except Exception as e:
        # Обработка исключений
        db.SET_log_record(f"Exception occurred: {e}")
        BufferSG.cancel_response = "Произошла непредвиденная ошибка."

order_history_menu = Dialog(
    Window(
        Jinja("""
{% for item in data[-5:] %}
<b><u>🔶 {{ item['order_name'] }}</u></b>
- <b>Статус:</b>  {{ item['status'] }}
- <b>Ссылка:</b> {{ item['link'] }}
- <b>Осталось выполнить:</b> {{ item['remains'] }}
- <b>Цена/Кол-во:</b> {{ item['price'] }} / {{ item['count'] }}
<b>Закрыть заказ</b> ▶️  /cancel_{{ item['order_id'] }}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
              
{% endfor %}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
<b>Показаны последние 5 заказов</b>
{% if cancel_response != None %}
              
<b>💬 {{cancel_response}} </b>
{% endif %}
        """),
        Cancel(
            Const("Назад")
        ),
        TextInput(
            id="input_cmd_cancel", 
            on_success=order_cancel,
            filter=input_orderid_filter
        ),
        parse_mode="HTML",
        state=OrderHistorySG.order_history_,
        disable_web_page_preview=True
    ),
    on_start=on_start,
    getter=getter
)
