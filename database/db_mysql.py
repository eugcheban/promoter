import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pymysql
from datetime import datetime
from config import Config
from api import Api
ap = Api()

class MySQLDatabase:
    cfg = Config()

    def __init__(self):
        self.host = self.cfg.db_host
        self.user = self.cfg.db_user
        self.password = self.cfg.db_password
        self.database = self.cfg.db_database
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, args=None):
        try:
            if not self.connection:
                self.connect()
            self.cursor.execute(query, args)
            self.connection.commit()
            return self.cursor.fetchall()  # Возвращаем результат запроса
        except Exception as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def register_user(self, user_id, user_name):
        try:
            reg_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Format datetime value
            query = "INSERT INTO promoter.users (reg_date, user_id, user_name, balance) VALUES (%s, %s, %s, %s)"
            args = (reg_date, user_id, user_name, 0)
            self.execute_query(query, args)
            print("User registered successfully.")
        except Exception as e:
            print(f"Error registering user: {e}")

    def check_user(self, user_id):
        try:
            query = "SELECT EXISTS(SELECT 1 FROM promoter.users WHERE user_id = %s)"
            args = (user_id,)
            result = self.execute_query(query, args)
            if result:
                return bool(result[0][0])
            else:
                return False
        except Exception as e:
            print(f"Error checking user: {e}")
            return False
    
    def GET_account_details(self, user_id):
        try:
            query = "SELECT user_name, balance FROM promoter.users WHERE user_id = %s"
            args = (user_id,)
            result = self.execute_query(query, args)
            if result:
                return {"user_id": user_id, "user_name": result[0][0], "balance": result[0][1]}
            else:
                return None
        except Exception as e:
            print(f"Error getting user details: {e}")
            return None

    def UPDATE_or_insert_services_official(self):
        data = ap.services()
        try:
            if not self.connection:
                self.connect()

            for item in data:
                service = item.get('service')
                name = item.get('name')
                type_ = item.get('type')
                rate = item.get('rate')
                min_ = item.get('min')
                max_ = item.get('max')
                dripfeed = item.get('dripfeed')
                refill = item.get('refill')
                cancel = item.get('cancel')
                category = item.get('category')

                query = """
                    INSERT INTO services_official (service, name, type, rate, min, max, dripfeed, refill, cancel, category, sys_date_update) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
                    ON DUPLICATE KEY UPDATE 
                    name=VALUES(name), type=VALUES(type), rate=VALUES(rate), min=VALUES(min), max=VALUES(max), 
                    dripfeed=VALUES(dripfeed), refill=VALUES(refill), cancel=VALUES(cancel), category=VALUES(category), sys_date_update=CURRENT_TIMESTAMP
                """
                args = (service, name, type_, rate, min_, max_, dripfeed, refill, cancel, category)
                self.execute_query(query, args)

            print("Services updated successfully.")
        except Exception as e:
            print(f"Error updating services: {e}")

    def GET_services_name_rates(self):
        try:
            if not self.connection:
                self.connect()

            query = "SELECT service, name, rate FROM services_local"
            result = self.execute_query(query)
            
            services_name_rates = {}
            for row in result:
                service = str(row[0])  # Преобразование в строку с добавлением кавычек
                name = str(row[1])
                rate = str(row[2]).strip('Decimal')  # Преобразование в строку без Decimal и удаление пробелов
                services_name_rates[service] = [name, rate]  # Добавление в словарь
            
            return services_name_rates

        except Exception as e:
            print(f"Error getting services and rates: {e}")
            return {}

    def GET_services_official(self):
        try:
            if not self.connection:
                self.connect()  # Подключение к базе данных, если не подключено

            query = "SELECT service, name, type, min, max, dripfeed, refill, cancel, category FROM services_official"
            result = self.execute_query(query)  # Выполнение запроса

            services_info = {}
            columns = ['service', 'name', 'type', 'min', 'max', 'dripfeed', 'refill', 'cancel', 'category']
            
            for row in result:
                service_data = {}
                for index, column_name in enumerate(columns[1:]):  # Начинаем с индекса 1, чтобы пропустить столбец 'service'
                    service_data[column_name] = row[index + 1]  # Используем индекс + 1 для получения данных из row
                service_name = row[0]  # Используем первый столбец (service) в качестве ключа
                services_info[str(service_name)] = service_data

            return services_info  # Возврат словаря с информацией о услугах

        except Exception as e:
            print(f"Error getting official services: {e}")
            return {}

    def SET_log_record(self, message):
        try:
            if not self.connection:
                self.connect()  # Подключение к базе данных, если не подключено

            # Получаем текущую дату и время
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Формируем SQL-запрос для добавления записи в таблицу logs
            query = f"INSERT INTO logs (message, date) VALUES ('{message}', '{current_date}')"

            # Выполняем запрос
            self.execute_query(query)

        except Exception as e:
            print(f"Error inserting log record: {e}")

    def SET_order_record(self, id_serv, user_id, count, price, order_id, link, order_name, order_category):
        try:
            if not self.connection:
                self.connect()  # Подключение к базе данных, если не подключено

            # Получаем текущую дату и время
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Формируем SQL-запрос для добавления записи в таблицу orders
            query = f"INSERT INTO order_history (date, id_serv, user_id, count, price, status, order_id, link, order_name, order_category) VALUES ('{current_date}', {id_serv}, {user_id}, {count}, {price}, 'NEW', {order_id}, '{link}', '{order_name}', '{order_category}')"
            
            # Выполняем запрос
            self.execute_query(query)

        except Exception as e:
            print(f"Error inserting order record: {e}")

    def SET_new_balance(self, user):
        try:
            if not self.connection:
                self.connect()  # Подключение к базе данных, если не подключено

            # SQL-запрос для обновления баланса пользователя
            update_query = "UPDATE users SET balance = %s WHERE user_id = %s"
            self.cursor.execute(update_query, (user["balance"], user["user_id"]))
            
            self.connection.commit()
            print(f"Баланс для пользователя {user['user_id']} успешно обновлен.")

        except Exception as e:
            print(f"user_id = {user['user_id']} Ошибка при обновлении баланса:", e)

    def GET_order_history(self, user_id):
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            if not self.connection:
                self.connect()  # Подключение к базе данных, если не подключено

            # SQL-запрос для получения истории ордеров для конкретного пользователя
            query = "SELECT id, date, id_serv, count, price, status, order_id, last_update, remains, link, order_name, order_category FROM order_history WHERE user_id = %s"

            # Выполняем запрос с переданным user_id
            result = self.execute_query(query, (user_id,))

            # Создаем список для хранения объектов истории ордеров
            order_history = []

            # Перебираем результат запроса и создаем объекты истории ордеров
            for row in result:
                status = None
                if row[5] == "Pending":
                    status = "Подготовка"
                elif row[5] == "NEW":
                    status = "Новый"
                elif row[5] == "Closed":
                    status = "Закрыт"
                elif row[5] == "":
                    status = "Новый"
                order = {
                    "id": row[0],
                    "date": row[1],
                    "id_serv": row[2],
                    "count": row[3],
                    "price": row[4],
                    "status": row[5],
                    "order_id": row[6],
                    "last_update": row[7],
                    "remains": row[8],
                    "link": row[9],
                    "order_name": row[10],
                    "order_category": row[11]
                }
                order_history.append(order)

            for el in order_history:
                order_status = ap.status(el["order_id"])
                el["status"] = order_status["status"]
                el["remains"] = order_status["remains"]
                el["last_update"] = current_date

            return order_history

        except Exception as e:
            print(f"Error getting order history: {e}")
            return []


# Пример использования:
if __name__ == "__main__":
    db = MySQLDatabase()
    db.connect()
    user_id = 7150119630

    #db.UPDATE_or_insert_services_official()
    order_history = db.GET_services_name_rates()
    print(order_history)
