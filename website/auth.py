from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user_provided_email = request.form.get('email')
        user_provided_password = request.form.get('password1')

        user = User.query.filter_by(email=user_provided_email).first()
        if user:
            if check_password_hash(user.password, user_provided_password):
                flash('Logged in successfully!', category = 'success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again.', category ='error')
        else:
            flash('Email does not exist.', category= 'error')

    data = request.form
    print(data)
    return render_template("login.html", boolean = True )

@auth.route('/logout')
@login_required
def logout():
    logout_user
    return redirect(url_for('auth.login'))

@auth.route('/sign-up',methods =['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        # Checks whether if email already exist in the database
        if user:
            flash('Email already exists!', category='error')
        # Checks for the inputs meet certain criteria
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.',category='input_error')
        elif len(first_name) < 2:
            flash('First name must be greater than 2 characters.',category='input_error')
        elif password1 != password2:
            flash('Passwords does not match',category='input_error')
        elif len(password1) < 7:
            flash('Passwords must be greater than 7 characters',category='input_error')
        else:
            # add user to database
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1,method ='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # Login the user after signing up
            login_user(user, remember=True)
            flash('Account created!',category='success')
            return redirect(url_for('views.home'))
        
    return render_template("sign_up.html")