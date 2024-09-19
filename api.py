import sys, os
import json
import requests
from config import Config

class Api:
    def __init__(self):
        config = Config()
        self.api_url = 'https://smmpanelus.com/api/v2'
        self.api_key = config.SMM_TOKEN

    def order(self, data):
        post = {**{'key': self.api_key, 'action': 'add'}, **data}
        return requests.post(self.api_url, data=post).json()

    def status(self, order_id):
        post_data = {'key': self.api_key, 'action': 'status', 'order': order_id}
        return requests.post(self.api_url, data=post_data).json()

    def multiStatus(self, order_ids):
        post_data = {'key': self.api_key, 'action': 'status', 'orders': ','.join(map(str, order_ids))}
        return requests.post(self.api_url, data=post_data).json()

    def services(self):
        post_data = {'key': self.api_key, 'action': 'services'}
        return requests.post(self.api_url, data=post_data).json()

    def refill(self, order_id):
        post_data = {'key': self.api_key, 'action': 'refill', 'order': order_id}
        return requests.post(self.api_url, data=post_data).json()

    def multiRefill(self, order_ids):
        post_data = {'key': self.api_key, 'action': 'refill', 'orders': ','.join(map(str, order_ids))}
        return requests.post(self.api_url, data=post_data).json()

    def refillStatus(self, refill_id):
        post_data = {'key': self.api_key, 'action': 'refill_status', 'refill': refill_id}
        return requests.post(self.api_url, data=post_data).json()

    def multiRefillStatus(self, refill_ids):
        post_data = {'key': self.api_key, 'action': 'refill_status', 'refills': ','.join(map(str, refill_ids))}
        return requests.post(self.api_url, data=post_data).json()

    def cancel(self, order_id):
        post_data = {'key': self.api_key, 'action': 'cancel', 'order': order_id}
        return requests.post(self.api_url, data=post_data).json()

    def balance(self):
        post_data = {'key': self.api_key, 'action': 'balance'}
        return requests.post(self.api_url, data=post_data).json()

def save_services_to_file(api, file_path):
    services = api.services()
    # Преобразование данных в читаемый формат
    services_readable = json.dumps(services, ensure_ascii=False, indent=4)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(services_readable)


if __name__ == "__main__":
    # Пример использования
    api = Api()
    print(os.environ.get('SMM_TOKEN'))
    save_services_to_file(api, 'services_smm.json')
    #services = api.services()  # Возвращает все услуги
    order_info = {
        "service": 32855,
        "link": "",
        "quantity": 100,
        "runs": None,
        "interval": None,
        "hashtag": None,
        "comments": None
    }

    # Добавление заказа
    #order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'runs': 2, 'interval': 5})  # По умолчанию
    #order = api.order({'service': 1, 'link': 'http://example.com/test', 'comments': "good pic\ngreat photo\n:)\n;"})  # Пользовательские комментарии
    #order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'hashtag': "test"})  # Упоминания хэштега
    #order = api.order({'service': 1, 'link': 'http://example.com/test'})  # Пакет
    #order = api.order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'runs': 10, 'interval': 60})  # Постепенная публикация
    # И т.д. для остальных примеров

    #status = api.status(order['order'])  # Возвращает статус, стоимость, остаток, количество начальных, валюту
    #statuses = api.multiStatus([1, 2, 3])  # Возвращает статусы заказов, стоимости, остатки, количество начальных, валюту
    #refill = api.multiRefill([1, 2])
    #refill_ids = [r['refill'] for r in refill]
    #if refill_ids:
    #    refill_statuses = api.multiRefillStatus(refill_ids)