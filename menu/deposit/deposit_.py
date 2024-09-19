from aiogram_dialog import Dialog, StartMode, Window, DialogManager
from aiogram_dialog.widgets.kbd import Start, Cancel, Button, Url
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Jinja
from aiogram_dialog.widgets.input import TextInput
from functools import partial
from magic_filter import F
from database.db_mysql import MySQLDatabase
from menu.states import (
    SubscribersSG, BotsActivationSG, ViewsSG, ServicesSG, DepositSG, AccountDetails,
    ReactionsSG, VotesSG, SharesSG, MainSG, DevSG, SubscribersStableSG, OrderSG, ServicesData
)
from config import Config


db = MySQLDatabase()
config = Config()
msg = """
Введите сумму в долларах для пополнения, целое число.
"""



msg_filter = None

prices = ServicesData.services_local

invoice = None

async def getter(dialog_manager: DialogManager, **kwargs):
    link = DepositSG.deposit_link
    msg_proceeding = f"Ваша заявка создана, платеж ожидает подтверждения.\n {link} \n Платеж будет зачислен в течении 10 минут после завершения транзакции."

    amount = 0
    creation = False
    return { 
        "amount": amount,
        "creation": creation,
        "msg_proceeding": msg_proceeding
    }

async def deposit_proceed(event, widget, dialog_manager: DialogManager, *_):
    # create invoice within api and go to next window
    user = event.from_user
    accountDetails = AccountDetails(user=user)
    amount = dialog_manager.find("input_deposit").get_value()
    if await DepositSG.create_invoice(amount=amount, user=user) == False:
        print(f"Deposit proceed error - def deposit_proceed")
        db.SET_log_record(f"Invoice created from user {accountDetails.info['user_id']} / {accountDetails.info['user_name']} with amount {amount}")
        #await dialog_manager.switch_to(DepositSG.deposit_fail_)
    else:
        await dialog_manager.switch_to(DepositSG.deposit_invoice_)


async def input_deposit_filter(message: str) -> bool:
    try:
        int(message.text) or float(message.text)
        return True
    except ValueError:
        return False

debosit_menu = Dialog(
    Window(
        Const(msg),
        TextInput(
            id="input_deposit", 
            on_success=deposit_proceed,
            filter=input_deposit_filter
        ),
        Cancel(Const("Назад")),
        state = DepositSG.deposit_,
        getter=getter
    ),
    Window(
        Jinja("{{ msg_proceeding }}"),
        Cancel(
            Const("Отмена")
        ),
        Cancel(
            Const("В главное меню")
        ),
        state=DepositSG.deposit_invoice_,
        getter=getter
    ),
    Window(
        Const("Ошибка при создании инвойса, обратитесь к администратору."),
        Url(
            Const("Админ"),
            Const(config.admin)
        ),
        Cancel("В главное меню"),
        state=DepositSG.deposit_fail_
    )
)

