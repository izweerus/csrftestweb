from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from flask_wtf.csrf import CSRFProtect
from .models import User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username, balance=current_user.balance)

@main.route('/deposit1')
@login_required
def deposit1():
    return render_template('depositpost.html', balance=current_user.balance)

@main.route('/deposit1/<int:amount>/<string:account>')
@login_required
def deposit1_get(amount, account):
    user = db.session.query(User).filter(User.username==current_user.username).first()
    # User.query.filter_by(username=current_user.username).first()
    new_amount = user.balance-amount
    user.balance = new_amount
    db.session.commit()

    return render_template('depositpost.html', message="The deposit was succesful", balance=user.balance)


@main.route('/deposit1', methods=['POST'])
@login_required
def deposit1_form():
    amount = int(request.form.get('amount'))
    account = request.form.get('account')
    user = db.session.query(User).filter(User.username==current_user.username).first()
    new_amount = user.balance-amount
    user.balance = new_amount
    db.session.commit()

    return render_template('depositpost.html', message="The deposit was succesful", balance=user.balance)

@main.route('/deposit2')
@login_required
def deposit2():
    return render_template('depositget.html', balance=current_user.balance)

@main.route('/depositGet')
@login_required
def depositGet():
    amount = int(request.args.get('amount'))
    account = request.args.get('account')
    user = db.session.query(User).filter(User.username==current_user.username).first()
    new_amount = user.balance-amount
    user.balance = new_amount
    db.session.commit()
    return render_template('depositget.html', balance=user.balance)

@main.route('/depositToken')
@login_required
def depositToken():
    return render_template('depositToken.html', balance=current_user.balance)

@main.route('/depositToken', methods=['POST'])
@login_required
def depositToken_form():
    amount = int(request.form.get('amount'))
    account = request.form.get('account')
    csrf = request.form.get('csrf_token')
    user = db.session.query(User).filter(User.username==current_user.username).first()
    new_amount = user.balance-amount
    user.balance = new_amount
    db.session.commit()

    return render_template('depositToken.html', message="The deposit was succesful", balance=user.balance)
