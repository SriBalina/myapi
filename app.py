from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_ghw():
    return "<p>HELLO WORLD</p>"