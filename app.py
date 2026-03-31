"""
Flask Login & Registration Web Application
Developed by: Arsh Sandhi | 4AI1 Batch 2
"""

import json
import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "arsh_sandhi_secret_key_4AI1"

USERS_FILE = "users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if not username or not password:
            flash("Please fill in all fields.", "error")
            return render_template("login.html")
        users = load_users()
        if username in users and users[username] == password:
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password. Please try again.", "error")
            return render_template("login.html")
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()
        if not username or not password:
            flash("Please fill in all fields.", "error")
            return render_template("register.html")
        if len(username) < 3:
            flash("Username must be at least 3 characters long.", "error")
            return render_template("register.html")
        if len(password) < 4:
            flash("Password must be at least 4 characters long.", "error")
            return render_template("register.html")
        users = load_users()
        if username in users:
            flash(f'Username "{username}" is already taken. Please choose another.', "error")
            return render_template("register.html")
        users[username] = password
        save_users(users)
        flash("Account created successfully! You can now log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    if "username" not in session:
        flash("Please log in to access the dashboard.", "error")
        return redirect(url_for("login"))
    username = session["username"]
    return render_template("dashboard.html", username=username)


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
