from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed   # these will allow us to update png file

from flask_login import current_user
from companyblog.models import User

class LoginForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('PassWord', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('PassWord', validators=[DataRequired(),EqualTo('pass_confirm', message= 'Passwords must match.')])
    pass_confirm = PasswordField('Confirm PassWord', validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been registered already!")
        
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username has been registered already!")

class UpdateUserForm(FlaskForm):
    
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['png', 'jpg'])])

    submit = SubmitField('Update Profile')

    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username has been registered already!")
        
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has been registered already!")
