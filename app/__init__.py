from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from settings import Config

db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'user.login'

mail = Mail()

from app.user.models import User


@login_manager.user_loader
def load_user(user_id: int):
    return db.session.execute(db.select(User).where(User.id == user_id)).scalar()


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager.init_app(app)
mail.init_app(app)


from app.user import user
from app.email import email
from app.routes import *

app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(email, url_prefix="/mail")
