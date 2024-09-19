import sys, os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.db_host = os.environ.get('host')
        self.db_user = os.environ.get('user')
        self.db_password = os.environ.get('password')
        self.db_database = os.environ.get('database')
        self.SMM_TOKEN = os.environ.get('SMM_TOKEN')
        self.TOKEN = os.environ.get('TOKEN')
        self.admin = os.environ.get('admin')

    def print_param(self):
        print(f'db_host = {self.db_host}')
        print(f'db_user = {self.db_user}')
        print(f'db_password = {self.db_password}')
        print(f'db_database = {self.db_database}')
        print('='*80)

if __name__ == '__main__':
    c = Config()
    c.print_param()
