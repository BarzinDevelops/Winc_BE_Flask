# Do not modify these lines
__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

# Add your code after this line


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<p>Home, sweet home.</p>"""

@app.route("/greet/")
def greet():
    return """<h1>Hello, world!</h1>
        <p>This is the '/greet' route page</p>
    """

@app.route("/greet/<example_name>")
def greet_name(example_name):
    return f"""<h1>Hello, {example_name}!</h1>"""

if __name__ == "__main__":
    app.run(debug=True)