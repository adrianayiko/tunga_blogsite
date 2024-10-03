from flask import app, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from flask_login import LoginManager
from . import auth
from .forms import LoginForm, RegisterForm
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('blog.index'))
        else:
            flash('Invalid credentials')
    return render_template('login.html', form=form)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        from .. import db  # Import db here to avoid circular import
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
