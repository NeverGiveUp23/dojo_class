from ninja_app import app

from flask import render_template, redirect, request, session

# from ninja_app.models.login_reg_model import Login
from ninja_app.models.dojo_model import Dojo
from ninja_app.models.ninja_model import Ninja

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def users():
    return render_template("dojos.html",dojos=Dojo.get_all_dojos())


@app.route('/dojos/new')
def new():
    return render_template("dojos.html")

@app.route('/user/create',methods=['POST'])
def create():
    #setting up the validation to pass through
    if not Dojo.validate_name(request.form):
        return redirect('/dojos')
    #else no errors run this code
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/show/<name>')
def show_dojo(name):
  show_dojo = {
    "name" : name
  }
  ninjas = Ninja.show_all_ninjas(show_dojo)
  return render_template('show_dojo_ninja.html', show_dojo = show_dojo, ninjas = ninjas)

@app.route('/login')
def login_ninja():
  return render_template('login_reg.html')