from . import auth
from flask import render_template
from .forms import signUpForm

@auth.route('/signup')
def signup():
  form = signUpForm()
  
  return render_template("signup.html")