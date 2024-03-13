from flask import Blueprint,render_template,request,redirect, url_for, jsonify

views=Blueprint(__name__,"views")

@views.route('/')
def home():
    return render_template("index.html")

#accessing using query perameters
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html",name=name)

@views.route("/json")
def get_json():
    return jsonify({'name':'pavi','age':20})

@views.route("/go-home")
def go_home():
    return redirect(url_for("views.get_json"))