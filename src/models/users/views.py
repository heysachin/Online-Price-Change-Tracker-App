

# Created by Sachin Dev on 01/06/18

from flask import Blueprint, request, render_template, session, url_for
from werkzeug.utils import redirect
from models.users.user import User
import models.users.errors as UserErrors
import models.users.decorators as user_decorators

user_blueprint = Blueprint('users',__name__)


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/login.jinja2")

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for(".user_alerts"))
        except UserErrors.UserError as e:
            return e.message

    return render_template("users/register.jinja2")


@user_blueprint.route('/alerts')
def user_alerts():
    user = User.find_by_email(session['email'])
    return render_template("users/alerts.jinja2", alerts=user.get_alerts())


@user_blueprint.route('/logout')
def logout_user():
    session['email'] = None
    return redirect(url_for('home'))


@user_blueprint.route('/check_alerts/<string:user_id>')
@user_decorators.requires_login
def check_user_alerts(user_id):
    pass