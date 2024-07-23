import os


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///db_{BASE_DIR.split("/")[-1]}.db'
    SECRET_KEY = 'your secret key'

    MAIL_SERVER = 'smtp.ukr.net'
    MAIL_PORT = 2525    # 465

    MAIL_USERNAME = os.getenv("MAIL_EMAIL")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    MAIL_DEFAULT_SENDER = os.getenv("MAIL_EMAIL")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
