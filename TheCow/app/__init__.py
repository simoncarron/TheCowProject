from flask import render_template, Flask, session
from .templates.auth import auth


app = Flask(__name__)

app.register_blueprint(auth.bp)


@app.route('/')
def index():
    if True:
        return render_template('pricing/index.html', title="Home", user=session)


@app.route('/auth')
def auth():
    if True:
        return render_template('auth/index.html', title="Home", user=session)