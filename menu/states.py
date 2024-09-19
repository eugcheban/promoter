from aiogram.filters.state import State, StatesGroup
from database.db_mysql import MySQLDatabase
from decimal import Decimal
import json
import plisio
import secrets
import string
from fastapi import FastAPI, Request, HTTPException
db = MySQLDatabase()

from api import Api

ap = Api()

class MainSG(StatesGroup):
    main = State()

class SubscribersSG(StatesGroup):
    subscribers_ = State()

class SubscribersStableSG(StatesGroup):
    stable = State()
class SubscribersCheapSG(StatesGroup):
    cheap = State()
class SubscribersRefillSG(StatesGroup):
    refill = State()
class SubscribersPremiumSG(StatesGroup):
    premium = State()

class BotsActivationSG(StatesGroup):
    bots_ = State()

class ViewsSG(StatesGroup):
    views_ = State()
    views_post = State()
    views_lastorfuture = State()
    views_last = State()
    views_future = State()
    views_shorts = State()

class ViewsPostSG(StatesGroup):
    views_post = State()
class ViewsLastorfutureSG(StatesGroup):
    views_lastorfuture = State()
class ViewsLastSG(StatesGroup):
    views_last = State()
class ViewsFutureSG(StatesGroup):
    views_future = State()
class ViewShortsSG(StatesGroup):
    views_shorts = State()

class ReactionsSG(StatesGroup):
    reactions_ = State()
    reactions_post = State()
    reactions_lastorfuture = State()
    reactions_real = State()
    reactions_lastorfuturereal = State()
class ReactionsPostSG(StatesGroup):
    reactions_post = State()
class ReactionsLastorfutureSG(StatesGroup):
    reactions_lastorfuture = State()
class ReactionsRealSG(StatesGroup):
    reactions_real = State()
class ReactionsLastorfuturerealSG(StatesGroup):
    reactions_lastorfuturereal = State()

class VotesSG(StatesGroup):
    votes_ = State()

class SharesSG(StatesGroup):
    shares_ = State()

class DevSG(StatesGroup):
    dev_ = State()
    order_id = 0

class OrderSG(StatesGroup):
    order_ = State()
    main_dialog = State()
    link_window = State()
    quantity_window = State()
    order_proceed = State()
    link_window_msg = "Укажите ссылку на группу для накрутки"
    count_window_msg = "Укажите количество"

    available_balance = None
    order_name = None
    order_category = None
    order_rate = None
    order_id = None
    order_info = None
    link = None
    quantity = None
    total_price = None
    min_order = None
    max_order = None
    cancle = None
    dripfeed = None
    runs = 1
    interval = 0
    order_id_TO_cancel = 0

    order_placement_result = None

    def __init__(self, id):
        super().__init__()
        self.order_id = id
        self.order_info = None
    
    @classmethod
    async def update(cls, update, *args, **kwargs):
        cls.order_id = update["id"]
        official_info = ServicesData.services_official
        order_info = ServicesData.services_local

        if "link" in update and "quantity" in update:
            cls.link = update["link"]
            cls.quantity = update["quantity"]
        
        cls.order_name = official_info[cls.order_id]["name"]
        cls.order_rate = order_info[cls.order_id][1]
        cls.min_order = official_info[cls.order_id]["min"]
        cls.max_order = official_info[cls.order_id]["max"]
        cls.order_placement_result = None
        
    @classmethod
    async def place_order(cls, user, *args, **kwargs):
        order_info = {
            "service": cls.order_id,
            "link": cls.link,
            "quantity": cls.quantity
        }
        
        accountDetails = AccountDetails(user=user)
        order = ap.order(order_info)
        #order = { "order": 33760 }

        if 'error' not in order:
            db.SET_order_record(
                cls.order_id,
                user.id,
                cls.quantity,
                cls.order_rate,
                order['order'],
                cls.link,
                cls.order_name,
                cls.order_category
            )
            # correction of the balance after order placement
            total_price_decimal = Decimal(cls.total_price)
            accountDetails.info["balance"] -= total_price_decimal
            db.SET_new_balance(accountDetails.info)
            cls.order_placement_result = "Заказ был успешно размещен."
        else:
            str = F"Error (1021) while placing order of user ${order_info}, error ${order['error']}"
            str_fuser = F"Ошибка (1021) при оформлении заказа, обратитесь к администратору за поддержкой."
            db.SET_log_record(str)
            cls.order_placement_result = str_fuser
    
    @classmethod
    async def cancel_order(cls, *args, **kwargs):
        return False

    @classmethod
    async def reset(cls, *args, **kwargs):
        available_balance = None
        cls.link_window_msg = "Укажите ссылку на группу для накрутки"
        cls.count_window_msg = "Укажите количество"
        cls.order_name = None
        order_category = None
        cls.order_rate = None
        cls.order_id = None
        cls.order_info = None
        cls.link = None
        cls.quantity = None
        cls.total_price = None
        cls.min_order = None
        cls.max_order = None
        cls.cancle = None
        cls.dripfeed = None
        cls.runs = 1
        cls.interval = 0
        order_id_TO_cancel = 0


class ServicesData(StatesGroup):
    services_local = db.GET_services_name_rates()
    services_official = db.GET_services_official()

class AccountDetails(StatesGroup):
    # contains "user_id": / "user_name": / "balance":
    info = {
        "user_id": None,
        "balance": 0,
        "order_history": [],
        "user_name": None
    }

    def __init__(self, user, *args, **kwargs):
        # load invoices from DB
        #print("info 1 ", self.info)
        if not db.check_user(user.id):
            db.register_user(user.id, user.username)
        # Обновим данные по пользователю в StatesGroup
        self.info = db.GET_account_details(user.id)
        #print(self.info)
        self.info["user_name"] = user.username

    async def update(cls, *args, **kwargs):
        order_history = db.GET_order_history(cls.info["user_id"])
        cls.info["order_history"] = order_history

        #print(cls.info)

class OrderHistorySG(StatesGroup):
    list_1 = State()
    list_2 = State()
    list_3 = State()
    list_4 = State()
    list_5 = State()
    list_6 = State()
    list_7 = State()
    list_8 = State()
    list_9 = State()
    list_10 = State()
    states = [
        list_1, 
        list_2, 
        list_3, 
        list_4, 
        list_5, 
        list_6, 
        list_7, 
        list_8, 
        list_9, 
        list_10
    ]
    order_history_ = State()
    order_history_1 = State()

    input_msg_err = "Ошибка команды, попробуйте еще раз."

class ServicesSG(StatesGroup):
    services = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update()

    def check_id(self, service_id):
        if self.services:
            for obj in self.services:
                if obj.get('service') == service_id:
                    return True
        return False

    def get_service_category(self, id_service):
        for obj in self.services:
            if obj.get('service') == id_service:
                return obj.get('category')
        return 'Not found 1022'
    
    def update(self):
        input_file_path = 'services_smm.json'
        try:
            # Открываем файл JSON и загружаем его содержимое
            with open(input_file_path, 'r', encoding='utf-8') as file:
                objects = json.load(file)

            # Фильтруем объекты с категорией "Telegram"
            #self.telegram_services = [obj for obj in objects if obj.get('category') == 'Telegram']
            # Сохраняем обьекты в переменную класса - services
            self.services = objects

        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

class BufferSG(StatesGroup):
    cancel_response = None

class DepositSG(StatesGroup):
    app = FastAPI()
    api_key = 'ol31MAL4r3N41vK3_E3Fr6W-SqZp7MaRC0uA0Jt_p3Ey5GQVZwrzF4dGq2gOUkct'
    deposit_ = State()
    deposit_invoice_ = State()
    deposit_fail_ = State()
    
    deposit_link = None
    invoices = []

    def __init__(self, *args, **kwargs):
        # load invoices from DB
        
        return False

    @classmethod
    async def create_invoice(self, amount, user, **kwargs):
        alphabet = string.ascii_letters + string.digits
        order_number = ''.join(secrets.choice(alphabet) for _ in range(20))
        try:
            # Create an asynchronous Plisio client
            client = plisio.PlisioAioClient(self.api_key)

            # Define the required parameters for the invoice
            currency = plisio.CryptoCurrency.USDT_TRX  # You can change this to any other supported cryptocurrency
            source_currency = plisio.FiatCurrency.USD
            source_amount = amount  # Invoice amount in USD

            # Create an invoice using the invoice method
            invoice = await client.invoice(
                currency=currency,
                order_name=user.id,
                order_number=order_number,
                source_currency=source_currency,
                amount=source_amount
            )
            self.deposit_link = invoice.invoice_url
            
            # Retrieve invoice ID for further operations
            invoice_id = invoice.txn_id
            
            # Print invoice information
            print(f"Invoice created: {invoice}")
            
            return True
            db.SET_log_record(f"invoice created: {invoice}")
        except Exception as e:
            # Handle exceptions and print error message
            print(f"An error occurred: {e}")
        return False
    
    @app.post("/callback")
    async def callback_handler(self, request: Request):
        client = plisio.PlisioClient(api_key=self.api_key)
        # Получите данные из POST-запроса
        data = await request.json()

        # Проверьте подпись запроса для подтверждения его подлинности
        if not client.validate_callback(data):
            raise HTTPException(status_code=400, detail="Invalid callback signature")

        # Обработка платежа в зависимости от его статуса
        status = data.get("status")
        order_number = data.get("order_number")
        txn_id = data.get("txn_id")

        if status == "completed":
            # Обработка успешного платежа
            # Пример: Обновление статуса заказа в базе данных
            # update_order_status(order_number, "completed")
            print(f"Payment completed for order: {order_number} (txn_id: {txn_id})")
        elif status == "cancelled":
            # Обработка отмененного платежа
            # Пример: Отмена заказа в базе данных
            # cancel_order(order_number)
            print(f"Payment cancelled for order: {order_number} (txn_id: {txn_id})")
        else:
            # Обработка других статусов (pending, expired и т.д.)
            print(f"Unhandled payment status: {status} for order: {order_number} (txn_id: {txn_id})")

        # Вернуть успешный ответ
        return {"status": "success"}