from flask import render_template, request, redirect
from dojo_app import app
from dojo_app.models.dojo import Dojo
from dojo_app.models.ninja import Ninja

@app.route("/dojos")
def home():
    dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojos = dojos)

@app.route("/add_ninja")
def add_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos = dojos)

@app.route("/show_ninjas/<int:dojo_id>")
def show_ninjas(dojo_id):
    data = {
        'dojo_id': dojo_id
    }
    dojo = Dojo.get_one_dojo(data)
    ninjas = Ninja.get_all_ninjas_dojo(data)
    return render_template("ninjas.html", dojo=dojo, ninjas=ninjas)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    Ninja.create_ninja(data)
    return redirect('/dojos')










@app.route('/sucess', methods=["POST"])
def sucess():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.create_new(data)
    return redirect('/')
