from flask import Blueprint, session, render_template, request, redirect, url_for
import sys


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        attempted_username = request.form['email']
        attempted_password = request.form['password']

        if attempted_username == "simon@simon.com" and attempted_password == "simon":
            session['email'] = request.form['email']
            return redirect(url_for('index'))
        else:
            error = "Invalid credentials. Try Again."

    return redirect(url_for('auth'))


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
