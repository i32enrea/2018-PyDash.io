"""
Contains the different routes (web endpoints) that the pydash_web flask application can respond to.

The actual implementation of each of the routes' dispatching logic is handled by the respective 'controller' function.
"""

from flask_login import login_required

# from pydash_web import flask_webapp
from pydash_web.blueprint import bp
import pydash_web.controller as controller


# @flask_webapp.route("/")
# @flask_webapp.route("/login", methods=["GET", "POST"])
@bp.route("/")
@bp.route("/login", methods=["GET", "POST"])
def login():
    return controller.login()


# @flask_webapp.route("/logout")
@bp.route("/logout")
def logout():
    return controller.logout()


# @flask_webapp.route("/dashboard")
@bp.route("/dashboard")
@login_required
def dashboard():
    return controller.dashboard()
