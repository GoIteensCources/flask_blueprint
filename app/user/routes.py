from flask_login import login_user, login_required, logout_user

from app import db
from flask import render_template, request, flash, redirect, url_for
from .models import User
from .forms import SignUpForm, LoginForm
from werkzeug.security import (
    generate_password_hash,
    check_password_hash,
)
from . import user


@user.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).where(User.nickname == form.nickname.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("index"))
            flash("Wrong password")
            return redirect(url_for("user.login"))

        flash("Wrong nickname")
        return redirect(url_for("user.login"))

    return render_template("user/login_signup.html", form=form, title="Login")


@user.route("/signup/", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            flash("User currently exists")
            return redirect(url_for("user.login"))
        new_user = User(
            nickname = form.nickname.data,
            email = form.email.data,
            password = generate_password_hash(form.password.data)
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("user.login"))
    return render_template("user/login_signup.html", form=form, title="Signup")


@user.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
