from flask import Flask

from app.auth import auth
from app.tasks import tasks_bp

from app.models import db
from app.models import User

def create_app(config_file = 'settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(tasks_bp, url_prefix = '/tasks')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
