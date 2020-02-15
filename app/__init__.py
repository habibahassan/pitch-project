import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from config import DevConfig


app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


mail = Mail(app)


from app.users.routes import users
from app.posts.routes import posts
from app.main.routes import main



app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

# from flaskblog.users.routes import users
# from flaskblog.posts.routes import posts
# from flaskblog.main.routes import main


# app.register_blueprint(users)
# app.register_blueprint(posts)
# app.register_blueprint(main)