import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'  #os.environ['SECRET_KEY']
    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://gjpzgisoidlzjq:f68a52a8692ffbde6330710a1574b556492284372343e2596f1bf0a0e17f254b@ec2-34-248-148-63.eu-west-1.compute.amazonaws.com:5432/ddhodit3oa84i7'#os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["WTF_CSRF_ENABLED"] = True
    csrf = CSRFProtect(app)
    db.init_app(app)
    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    from .models import Posts

    admin = Admin(app, name='Pinocchio Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Posts, db.session))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    csrf.exempt(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    csrf.exempt(main_blueprint)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)
    csrf.exempt(blog_blueprint)

    from .blueCSRF import blueCSRF as blueCSRF_blueprint
    app.register_blueprint(blueCSRF_blueprint)

    return app
