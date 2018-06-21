

# Created by Sachin Dev on 01/06/18

from flask import Flask, render_template

from common.database import Database
from models.users.views import user_blueprint

app = Flask(__name__)
app.config.from_object('config')
app.secret_key='sachin'


@app.before_first_request
def _init_db():
    Database.initialize()


@app.route('/')
def home():
    return render_template('home.jinja2')


from models.users.views import user_blueprint
from models.stores.views import store_blueprint
from models.alerts.views import alert_blueprint
app.register_blueprint(user_blueprint, url_prefix="/users")
app.register_blueprint(store_blueprint, url_prefix="/stores")
app.register_blueprint(alert_blueprint, url_prefix="/alerts")