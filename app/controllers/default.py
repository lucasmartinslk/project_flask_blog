from app import app, db, lm
from flask_login import login_user, logout_user
from flask import render_template, flash, url_for, redirect
from app.models.forms import LoginForm
from app.models.tables import User


@lm.user_loader
def load_user(id):
  return User.query.filter_by(id=id).first()


@app.route("/")
@app.route("/index/")
def index():
    return render_template('index.html')


@app.route("/login", methods=["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logado!")
            return redirect(url_for("index"))
        else:
            flash("Login Inválido")

    return render_template('login.html', form=form)


@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
    r = User.query.filter_by(username='lukita').all()
    print(r)
    return "OK"


@app.route("/logout")
def logout():
    logout_user()
    flash("Desconectado")
    return redirect(url_for("index"))