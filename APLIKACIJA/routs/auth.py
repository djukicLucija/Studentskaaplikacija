from flask import Blueprint, render_template, request, redirect, session, url_for
import sqlite3

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return redirect('/login')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form["password"]  # ispravljeno ime promenljive
        conn = sqlite3.connect("baza.db")
        c = conn.cursor()
        c.execute("SELECT id, role FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()
        if result:
            session['user_id'] = result[0]
            session['username'] = username
            session['role'] = result[1]
            return redirect(f"/{session['role']}")
        else:
            error = "Pogrešni podaci"
    return render_template('login.html', error=error)

@auth_bp.route('/logout')  # dodata ruta za logout
def logout():
    session.clear()
    return redirect('/login')

