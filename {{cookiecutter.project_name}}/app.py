import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf.csrf import CSRFProtect

load_dotenv()

app = Flask(__name__)
csrf = CSRFProtect()
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
csrf.init_app(app)

@app.get("/")
def home():
    return render_template("home.html")
