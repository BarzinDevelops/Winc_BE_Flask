from flask import Flask, render_template, redirect, url_for, request
from data import blogs

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/home")
def home():
    return redirect(url_for('index'))
    # return redirect(url_for('index', title="Home"))

@app.route("/")
def index():
    title = request.args.get('title', 'Index')
    return render_template(f"index.html", title=title)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog", blogs=blogs)

if __name__ == "__main__":
    app.run(debug=True)