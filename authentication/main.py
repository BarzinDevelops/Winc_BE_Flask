import os

from flask import Flask, redirect, render_template, request, session, url_for, flash
from helpers import valid_login

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)

@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


""" @app.route("/login", methods=["GET", "POST"])
def login():
    error = request.args.get('error', None)
    
    if request.method == "POST":
        
        is_valid = valid_login( request.form['username'],
                                request.form['password'] )
        print(f"\nmain.py -> login()\nis_valid is BEFORE checking in login route: {is_valid}")
        print(f"\nmain.py -> login()\nis_valid[0] is BEFORE checking in login route: {is_valid[0]}\n")
        if is_valid[0]:
            print(f"\nmain.py -> login()\nVALID username is now: {is_valid[1]}\n\n")
            return render_template("dashboard.html", username=is_valid[1]) 
        else:
            error = 'Invalid username/password'
            flash(error)
            print(f"\nmain.py -> login()\nThe error is: {error}\n\n")
            return redirect(url_for("login"))
    else:
        print(f"\nmain.py -> login()\nRendering login template with error: {error}\n")
        return render_template(f"login.html", title="Login") """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        is_valid_user = valid_login(username, password)
        
        if not username.strip() == '' or not password.strip() == '':
            if is_valid_user[0]:
                session['username'] = is_valid_user[1] # storing username in session
                flash('Login successful!', 'success')
                return redirect(url_for("dashboard", user_name=is_valid_user[1]))
            else:
                flash('Invalid username/password', 'error')
        else:
            flash('Fill in a valid username/password', 'warning')

    return render_template("login.html")




@app.route("/dashboard/<user_name>")
def dashboard(user_name):
    return render_template(f"dashboard.html", user_name=user_name)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.pop('username', None) # removes username from session
    session.pop('_flashes', None) # removes flash messages from the current session
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)