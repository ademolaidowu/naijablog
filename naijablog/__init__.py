import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
# from dotenv import load_dotenv


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "Login"
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIl_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIl_PASSWORD")
mail = Mail(app)



from naijablog import routes