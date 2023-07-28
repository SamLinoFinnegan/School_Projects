__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index(name="Index"):
    return render_template("index.html", title=name)


@app.route("/home/")
def home():
    return redirect(url_for("index"))   

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/somewhere")
def something():
    return render_template("something.html", title="Dark web")
if __name__ == "__main__":
    app.run()
