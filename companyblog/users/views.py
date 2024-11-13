from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from companyblog import db
from companyblog.models import User, BlogPost
from companyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from companyblog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)

# crete views:

# register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form = form)

# login
@users.route('login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email= form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log in Success!')

            next = request.args.get('next') 

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)
        
        return render_template('login.html')


# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
# account (update UserForm)
# user's list of Blog Posts



