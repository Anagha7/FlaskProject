from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField ,TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ChatForm(FlaskForm):
   # name = Label('ChatApp')
    chatwin = TextAreaField('ChatApp')
    msg = StringField(default='Type Here')
    submit = SubmitField('Enter')
