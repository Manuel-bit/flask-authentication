from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class signUp(FlaskForm):
  username = StringField("username",[validators.DataRequired()])
  password = PasswordField("password", [validators.DataRequired(), validators.EqualTo("confirm", message='passwords must match')])
  confirm =  passwordfield("Confirm password",[validators.DataRequired()])
  submit = SumitField("sign up")
