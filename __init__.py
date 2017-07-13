from flask import Flask

app = Flask(__name__)

app.config["DATABASE"] = 'catAdopt.db'
app.config['DEBUG'] = True
app.config["SECRET_KEY"] = ""
app.config["USERNAME"] = ""
app.config["PASSWORD"] = ""

from app import views, models
