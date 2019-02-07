from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")
    
    
@app.route("/articles/")
def articles():

    data = select_all("articles")

    
    return render_template("articles.html",data=data)


@app.route("/articles/<int:id>")
def detail(id):
    if id == None:
        return redirect("articles")
    
    data = select_by_id("articles", id)
    
    return render_template("detail.html",data=data)
    
    
@app.route("/articles/<int:id>/edit")
def edit(id):
    data = select_by_id("articles", id)
    
    return render_template("edit.html",data=data)


@app.route("/articles/<int:id>/update", methods=["POST"])
def update(id):
    title = request.form.get("title")
    content = request.form.get("content")
    author = request.form.get("author")
    nowtime = str(datetime.now())
    
    _update("articles",id,"title",title)
    _update("articles",id,"content",content)
    _update("articles",id,"author",author)
    _update("articles",id,"created_at",nowtime)
    
    return redirect("/articles/{}".format(id))
    
@app.route("/articles/<int:id>/delete")
def delete(id):
    _delete("articles",id)
    
    return redirect("/articles")


@app.route("/articles/new")
def new():
    return render_template("new.html")
    
    
@app.route("/articles/new/create",methods=["POST"])
def create():
    title = request.form.get("title")
    content = request.form.get("content")
    author = request.form.get("author")
    nowtime = str(datetime.now())
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO {} (title, content,created_at,author) VALUES ('{}','{}','{}','{}')".format("articles",title,content,nowtime,author))
    conn.commit()
    conn.close()
    
    return redirect("/articles")
    
    
    
    
    
    
    
    
def select_all(table):
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute('SELECT * FROM {}'.format(table))
    data = cur.fetchall()
    
    conn.close()
    
    return data
    
def select_by_id(table, id):
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM {} WHERE id = {}".format(table, id))
    data = cur.fetchone()
    
    conn.close()
    return data

def _update(table,id,col,content):
    
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("UPDATE {} SET {} = '{}' WHERE id = {}".format(table,col,content,id))
    
    conn.commit()
    conn.close()
    
def _delete(table,id):
    
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM {} WHERE id = {}".format(table,id))
    
    conn.commit()
    conn.close()