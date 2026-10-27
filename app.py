
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>malek - le grand tete</h1>
    <p>trilili prilili kaka, brooty frooty</p>
    """
