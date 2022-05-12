from flask import render_template,redirect,url_for,flash,request
from . import auth
from .. import mail
from flask_mail import Message
from flask_login import login_user,logout_user,login_required,current_user
from .forms import LoginForm,SignUpForm
from ..models import User,Pitch

@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user =  User(email = form.email.data, username = form.username.data,password = form.password.data)
        user.save_user()
        try:
            msg = Message('Hello...Welcome to pitches.We are glad you joined us',sender=('esthertest@gmail.com'))
            msg.add_recipient(user.email)
            mail.send(msg)
        except Exception as e:
            print('failed')

        return redirect(url_for('auth.login'))
    
        title = "New Account"
    return render_template('sign_up.html',signup_form = form)

