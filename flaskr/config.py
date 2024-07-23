from datetime import timedelta
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'ABCD1234')
    MYSQL_USER = os.getenv('MYSQL_USER', 'dbs')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DB = os.getenv('MYSQL_DB', 'GOBUZZ')
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', '484213283363-0lr7vmgdk81h02f8e9p8pgalq1n9ov6v.apps.googleusercontent.com')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', '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')
    SQLITE_DB = os.getenv('SQLITE_DB', 'flaskr/instance/GOBUZZ.db')
    DB_TYPE = os.getenv('DB_TYPE', 'SQLITE')

    # SMTP Configuration for Gmail
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'nashl449@gmail.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'jhmo kefg bkqa syee')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'nashl449@gmail.com')

    # Session Configuration
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = './flask_session/'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
