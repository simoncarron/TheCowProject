from flask import render_template, Flask
import config

app = Flask(__name__)


@app.route('/')
def index():
    if session.get('user'):
        return "Hello World!"
    else:
        return render_template(config.AUTHENTIFICATION_TEMPLATE)
