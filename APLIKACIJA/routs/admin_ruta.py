from flask import Blueprint,render_template,request,redirect,session
import sqlite3

admin_bp=Blueprint('admin',__name__,url_prefix="/admin")

@admin_bp.route("/")
def dashboard():
    if session.get('role')!='admin':
        return redirect("/login")
    return render_template("admin.html")
@admin_bp.route("/add_user",methods=["POST"])

def add_user():
    if session.get('role')!='admin':
        return redirect("/login")
    username=request.form['username']
    password=request.form['password']
    role=request.form['role']
    conn=sqlite3.connect('baza.db')
    c=conn.cursor
    c.execute("INSERT INTO users (username,password,role) VALUES (?,?,?)",(username,password,role))
    conn.commit()
    conn.close()
    return redirect('/admin')
def add_subject():
    if session.get('role')!='admin':
        return redirect('/login')
    name=request.form['subject']
    conn=sqlite3.connect('baza.db')
    c=conn.cursor()
    c.execute("INSERT INTO subjects (name) VALUES (?)",(name))
    conn.commit()
    c.close()
    return redirect("/admin")