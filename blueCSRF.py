from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from flask_wtf.csrf import CSRFProtect
from .models import User
from . import db

blueCSRF = Blueprint('blueCSRF', __name__)

@blueCSRF.route('/depositCSRF')
@login_required
def depositCSRF():
    return render_template('depositCSRF.html', balance=current_user.balance)

@blueCSRF.route('/depositCSRF', methods=['POST'])
@login_required
def depositCSRF_form():
    amount = int(request.form.get('amount'))
    account = request.form.get('account')
    csrf = request.form.get('csrf_token')
    user = db.session.query(User).filter(User.username==current_user.username).first()
    new_amount = user.balance-amount
    user.balance = new_amount
    db.session.commit()

    return render_template('depositCSRF.html', message="The deposit was succesful", balance=user.balance)
