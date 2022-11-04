from ninja_app import app

from flask import render_template, redirect, request, session

from ninja_app.models.ninja_model import Ninja
from ninja_app.models.dojo_model import Dojo

@app.route('/ninjas')
def add_ninja():
  return redirect('/new/ninjas')

@app.route('/new/ninjas')
def ninja_form():
  return render_template("new_ninja.html",dojos = Dojo.get_all_dojos())



@app.route('/ninjas/new')
def add_dojo():
  return render_template("dojos.html")

@app.route('/ninja/create',methods=['POST'])
def create_ninja():
  #an if statement for the form if not filled out correctly
    if not Ninja.validate_ninja(request.form):
      return redirect('/new/ninjas')
    if not Ninja.validate_email(request.form):
      return redirect('/new/ninjas')
    #this will save if the form was filled out correctly
    Ninja.save_ninja(request.form)
    return redirect('/dojos')
 
