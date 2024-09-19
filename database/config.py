from configparser import ConfigParser
import os

class Config:
    def __init__(self):
        self.db_host = 'localhost'
        self.db_user = 'chopa'
        self.db_password = ''
        self.db_database = 'promoter'

    def print_param(self):
        print(f'db_host = {self.db_host}')
        print(f'db_user = {self.db_user}')
        print(f'db_password = {self.db_password}')
        print(f'db_database = {self.db_database}')
        print('='*80)

if __name__ == '__main__':
    c = Config()
    c.print_param()
