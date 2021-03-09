from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User, Posts
from . import db

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def post():
    blog = Posts.query.all()
    return render_template('blog.html', posts=blog)


@blog.route('/blog', methods=['POST'])
@login_required
def post_form():
    name = request.form.get('name')
    text = request.form.get('text')
    post = Posts(name, text)
    db.session.add(post)
    db.session.commit()
    blog = Posts.query.all()
    return render_template('blog.html', posts=blog)
