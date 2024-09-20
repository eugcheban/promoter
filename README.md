# promoter

Telegram bot, which represents an idea, of selling 3-rd partie services (Telegram SEO via API), with your own markup. 

## Prepare to run
1. Clone repository `git clone https://github.com/eugcheban/promoter`
2. Import database structure `dump.sql` into your MySQL
3. Create environment `python -m venv promoter`
4. Install dependencies `pip install -r requirements.txt`

From the features for work, you should update services in a semi-automated mode, which includes downloading the current services and rates using methods from `api.py`. To save this data into a file, use the `save_services_to_file()` function. After that, in manual mode, prepare and upload this data to the database into a table called `services_official`, from which you can copy the data into the `services_local` table with your own markup.

## Sample .env

```
TOKEN = "telegram bot token"
SMM_TOKEN = "api token"
admin = "https://t.me/username"

[db_mysql]
host = localhost
user = user
password = ''
database = database name
```
