from ninja_app import app

from flask import render_template, redirect, request, session

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
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')
  
@app.route('/show/<name>')
def show_dojo(name):
  show_dojo = {
    "name" : name
  }
  ninjas = Ninja.show_all_ninjas(show_dojo)
  return render_template('show_dojo_ninja.html', show_dojo = show_dojo, ninjas = ninjas)