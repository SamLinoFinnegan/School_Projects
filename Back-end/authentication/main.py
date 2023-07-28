import os

from flask import Flask, redirect, render_template, request, session, url_for, flash
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)
session 

@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    if "user" in session:
        user = session["user"]
        return render_template("index.html", title="Home", user=True, user_name=user)
    else:
        
        return render_template("index.html", title="Home", user=False)

@app.route("/about")
def about():
    if "user" in session:
        user = session["user"]
        return render_template("about.html", title="About", user=True, user_name=user)
    else:
        return render_template("about.html", title="About", user=False)



@app.route("/lon")
def lon():
    if "user" in session:
        user = session["user"]
        return render_template("lon.html", title="League of Nations", user=True, user_name=user)
    else:
        flash("You must be logged in to access this page")
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form['username']
        password = request.form['password']
        user_database = get_users()
        
        hashed_password = hash_password(password)
        if user in user_database and hashed_password == user_database.get(user):
            session["user"] = user
            return redirect(url_for("dashboard"))
        else:
            flash("User not in database", "info")
            return render_template("login.html", title="Log In")
    else:   
        return render_template("login.html", title="Log In")


@app.route("/dashboard")
def dashboard():
    if "user" in session:
        user = session["user"]
        if user == "Bob":
            img = "data:image/jpeg;base64,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"
        elif user == "Alice":
            img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRwxaPaRhy2zLdjbqQhPuEAfeJvO6tcCJv7w&usqp=CAU"
        flash("You have been successfuly logged in!")
        return render_template("dashboard.html", usr=user, image=img)
    else:
        flash("You must be logged in to access this page")
        return redirect(url_for("login", title="Log In"))


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if "user" in session:
        session.pop("user" , None)
        flash("You have been successfuly logged out!")
        return redirect(url_for("index", title="Home"))
   


if __name__ == "__main__":
    app.run()