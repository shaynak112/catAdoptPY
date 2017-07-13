#!/usr/bin/env python2.x

print "Content-type: text/html\n\n"
print "Hello World"

import sqlite3
from flask import Flask, render_template, g, url_for, flash, request, redirect




app = Flask(__name__)


#DB info

DATABASE = 'catAdopt.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

@app.before_request
def before_request():
    g.db = connect_db()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


#views

@app.route('/')
def homepage():
    adoptTitle = "Cat Adoption"
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from cats where adopted='no' order by rowid DESC limit 3")   
    rows = cur.fetchall(); 
    return render_template('index.html',rows = rows, adoptTitle=adoptTitle)

@app.route('/adoptApplication')
def adoptApplication():
	adoptTitle = "Cat Adoption"
	return render_template('adoptApplication.html', adoptTitle=adoptTitle)

@app.route('/appThanks')
def appThanks():
	adoptTitle = "Cat Adoption"
	return render_template('appThanks.html', adoptTitle=adoptTitle)

@app.route('/searchCatsPage')
def searchCatsPage():
	adoptTitle = "Cat Adoption"
	return render_template('searchCatsPage.html',adoptTitle=adoptTitle)

@app.route('/allCats')
def allCats():
    adoptTitle = "Cat Adoption"
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from cats where adopted='no' order by rowid DESC")   
    rows = cur.fetchall(); 
    return render_template('allCats.html',rows = rows, adoptTitle=adoptTitle)

@app.route('/successStories')
def successStories():
	adoptTitle = "Cat Adoption"
	return render_template('successStories.html',adoptTitle=adoptTitle)

@app.route('/contact')
def contact():
	adoptTitle = "Cat Adoption"
	return render_template('contact.html', adoptTitle=adoptTitle)

@app.route('/allApplications')
def allApplications():
    adoptTitle = "Cat Adoption"
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from applications order by catName ASC")
    rows = cur.fetchall(); 
    return render_template('allApplications.html',rows = rows, adoptTitle=adoptTitle)



#methods

@app.route('/submitAdoptApp', methods = ['POST', 'GET'])
def submitAdoptApp():
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    appName = request.form['appName']
    appAge = request.form['appAge']
    appEmail = request.form['appEmail']
    appPhone = request.form['appPhone']
    appAddress = request.form['appAddress']
    appOccupation = request.form['appOccupation']
    appCatName = request.form['appCatName']
    appRefName = request.form['appRefName']
    appRefRelation = request.form['appRefRelation']
    appRefPhone = request.form['appRefPhone']
    cur.execute("INSERT INTO applications VALUES (?,?,?,?,?,?,?,?,?,?)", (appName, appAge, appEmail, appPhone, appAddress, appOccupation, appCatName, appRefName, appRefRelation, appRefPhone))
    con.commit()
    con.close()
    return redirect('/appThanks')


@app.route('/searchTrait', methods = ['POST', 'GET'])
def searchTrait():
    adoptTitle = "Cat Adoption"
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    searchTerm = request.form['searchTrait']
    cur.execute("SELECT * FROM cats WHERE (((trait1=searchTerm) OR (trait2=searchTerm) OR (trait3=searchTerm)) AND adopted='no') ORDER BY rowid DESC")
    rows = cur.fetchall(); 
    return render_template('searchTrait.html',rows = rows, adoptTitle=adoptTitle)

if __name__ == '__main__':
	app.run()
