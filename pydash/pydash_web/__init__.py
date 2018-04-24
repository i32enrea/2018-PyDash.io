"""
Entrypoint of `pydash_web`

Initializes a Flask web application, and loads the relevant configuration settings.
"""


from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from pydash_web.blueprint import bp as pydash_web_bp

from config import Config

import pydash_app
import pydash_app.user


flask_webapp = Flask(__name__, static_folder="../../pydash-front/build", static_url_path="")
flask_webapp.config.from_object(Config)
login_manager = LoginManager(flask_webapp)
flask_webapp.register_blueprint(pydash_web_bp)
flask_webapp.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(flask_webapp, resources={r"/api/*": {"origins": "*"}}, allow_headers=['Content-Type'], supports_credentials=True) # Only keep this line during development!


pydash_app.schedule_periodic_tasks()
pydash_app.start_task_scheduler()

@login_manager.user_loader
def load_user(user_id):
    print("Loading user {}".format(user_id))
    return pydash_app.user.maybe_find_user(user_id)


@flask_webapp.cli.command('seed', with_appcontext=False)
def seed_command():
    """Initializes our datastore with some preliminary values"""
    pydash_app.seed_datastructures()
