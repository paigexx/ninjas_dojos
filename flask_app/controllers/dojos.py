import re
from flask_app.models.ninja import Ninja
from flask_app import app
from flask import redirect, request, render_template
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def show_all_dojos():
    dojos = Dojo.show_dojos()
    print(dojos)
    return render_template("dojos.html", dojos = dojos)

@app.route("/dojos/create", methods =['POST', 'GET'])
def new_dojo():
    data = {
        "name": request.form["name"]
    }
    print(request.form)
    Dojo.create_dojo(data)
    return redirect("/")

@app.route("/dojos/<int:dojo_id>")
def dojo_with_ninjas(dojo_id):
    data = {
        'dojo_id': dojo_id
    }
    dojo = Dojo.get_dojo(data)
    return render_template("dojo_show.html", dojo = dojo)

@app.route("/dojos/ninja")
def add_ninja():
    dojos = Dojo.show_dojos()
    return render_template("new_ninja.html", dojos = dojos)

@app.route("/dojos/create_ninja", methods=['POST'])
def new_ninja():
    print(request.form)
    # pass the whole request.form over to the class method. a data dictionary will not work for the key ??
    Ninja.create_ninja(request.form)
    return redirect("/")


