import sqlite3
from flask import Flask, render_template, g, flash, request, redirect, url_for
from werkzeug import secure_filename
import datetime as dt
#activate_this = '/home/max/.virtualenvs/flask/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

#import sys
#sys.path.insert(0, '/home/max/Projekte/flask-upload')

app = Flask(__name__)

#photo upload setup

UPLOAD_FOLDER = '/static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

#photo upload info

#@app.route('/upload')
#def upload_file():
#   return render_template('upload.html')
    
#@app.route('/uploader', methods = ['GET', 'POST'])
#def uploader():
#   if request.method == 'POST':
#      f = request.files['file']
#      f.save(secure_filename(f.filename))
#      return 'file uploaded successfully'



#public

@app.route('/')
def homepage():
    adoptTitle = "Cat Adoption"
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from cats where adopted='no' order by rowid DESC limit 3")   
    rows = cur.fetchall();
    con2 = sqlite3.connect("catAdopt.db")
    con2.row_factory = sqlite3.Row
    cur2 = con2.cursor()
    cur2.execute("select * from cats where adopted='yes' order by rowid DESC limit 1")   
    rows2 = cur2.fetchall(); 
    return render_template('index.html',rows = rows,rows2=rows2,adoptTitle=adoptTitle)


@app.route('/adoptApplication', methods=['GET','POST'])
def adoptApplication():
    adoptTitle = "Cat Adoption"
    submitAdoptApp()
    return render_template('adoptApplication.html', adoptTitle=adoptTitle)


@app.route('/submitAdoptApp', methods=['GET','POST'])
def submitAdoptApp():
    print("running submit adopt app")
    try:
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
        dateApplied='2017-06-17'
        followUp='none'
        sucessful='pending'
        print (appName, appAge, appEmail, appPhone, appAddress, appOccupation, appCatName, dateApplied, sucessful)
        con = sqlite3.connect("catAdopt.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("INSERT INTO applications('fullName','age','email','phone','address','occupation','catName','refName','refRelationship','refPhone','dateApplied','followUp','sucessful') VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(appName,appAge,appEmail,appPhone,appAddress,appOccupation,appCatName,appRefName,appRefRelation,appRefPhone,dateApplied,followUp,sucessful))
        con.commit()
        print('entered')
        #return render_template('appThanks.html', adoptTitle=adoptTitle)
    except Exception as e:
        return(str(e))



@app.route('/appThanks')
def appThanks():
	adoptTitle = "Cat Adoption"
	return render_template('appThanks.html', adoptTitle=adoptTitle)



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
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from cats where adopted='yes' order by rowid DESC limit 8")   
    rows = cur.fetchall(); 
    return render_template('successStories.html',rows=rows,adoptTitle=adoptTitle)

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

#rescue side

@app.route('/rescueHome')
def rescueHome():
    return render_template('rescueHome.html')
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/rescueAddCat', methods=['GET','POST'])
def rescueAddCat():
    rescueSubmitCat()
    return render_template('rescueAddCat.html')

@app.route('/rescueSubmitCat',methods=['GET','POST'])
def rescueSubmitCat():
    print("New cat received")
    try:
        catName = request.form['catName']
        catAge = request.form['catAge']
        catGender = request.form['catGender']
        catBreed = request.form['catBreed']
        catColour = request.form['catColour']
        catTrait1 = request.form['catTrait1']
        catTrait2 = request.form['catTrait2']
        catTrait3 = request.form['catTrait3']
        catDescription = request.form['catDescription']
        imageURL = request.form['imageURL']
        catRescue = request.form['catRescue']
        adopted='no'
        print (catName,catAge,catGender,catBreed,catColour,catTrait1,catTrait2,catTrait3,catDescription,catRescue, adopted, imageURL)
        con = sqlite3.connect("catAdopt.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("INSERT INTO cats('name','age','gender','breed','colour','imageURL','trait1','trait2','trait3','description','adopted','rescue') VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(catName,catAge,catGender,catBreed,catColour,imageURL,catTrait1,catTrait2,catTrait3,catDescription,adopted,catRescue))
        con.commit()
        print ("Entered")
        #return redirect('/catAdded.html')
    except Exception as e:
        return(str(e))

@app.route('/catAdded')
def catAdded():
    return render_template('catAdded.html')


@app.route('/rescueViewApps')
def rescueViewApps():
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from applications where sucessful='pending' order by catName ASC")
    #cur.execute("select * from applications order by catName ASC")
    rows = cur.fetchall(); 
    con2 = sqlite3.connect("catAdopt.db")
    con2.row_factory = sqlite3.Row
    cur2 = con2.cursor()
    cur2.execute("select * from applications where sucessful='denied' order by catName ASC")
    rows2 = cur2.fetchall();
    con3 = sqlite3.connect("catAdopt.db")
    con3.row_factory = sqlite3.Row
    cur3 = con3.cursor()
    cur3.execute("select * from applications where sucessful='approved' order by catName ASC")
    rows3 = cur3.fetchall();
    con4 = sqlite3.connect("catAdopt.db")
    con4.row_factory = sqlite3.Row
    cur4 = con4.cursor()
    cur4.execute("select * from applications order by catName ASC")
    rows4 = cur4.fetchall();    
    return render_template('rescueViewApps.html',rows=rows,rows2=rows2,rows3=rows3,rows4=rows4)

@app.route('/rescueViewRescues')
def rescueViewRescues():
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from rescues order by rescueName ASC")
    rows = cur.fetchall(); 
    return render_template('rescueViewRescues.html',rows=rows)

@app.route('/rescueCatStatus')
def rescueCatStatus():
    catAdopted()
    catUpdateDescription()
    catRemoved()
    catFollowUp()
    return render_template('rescueCatStatus.html') #probably another page

@app.route('/catAdopted',methods=['GET','POST'])
def catAdopted():
    print("cat adopted")

    try:
        catName = request.form['catName']
        catRescue = request.form['catRescue']
        print(catName,catRescue)
        con = sqlite3.connect("catAdopt.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("update cats SET adopted='yes', description='This cat has successfully found a home!' where name='catName'")
        rows = cur.fetchall();
        con.commit()
        print ("adoption entered")
        return redirect('/rescueCatStatus')
    except Exception as e:
        return(str(e))

@app.route('/catUpdateDescription',methods=['GET','POST'])
def catUpdateDescription():
    print ("cat description")

    try:
        catName = request.form['catName']
        catRescue = request.form['catRescue']
        catDescription = request.form['catDescription']
        print(catName,catRescue)
        con = sqlite3.connect("catAdopt.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("update cats SET description=catDescription where name='catName'")
        rows = cur.fetchall();
        con.commit()
        print ("description entered")
        return redirect('/rescueCatStatus.html')
    except Exception as e:
        return(str(e))

@app.route('/catRemoved',methods=['GET','POST'])
def catRemoved():
    print ("cat removed")

    try:
        catName = request.form['catName']
        catRescue = request.form['catRescue']
        print(catName,catRescue)
        con = sqlite3.connect("catAdopt.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("delete cats where name='catName'")
        rows = cur.fetchall();
        con.commit()
        print ("removed cat")
        return redirect('/rescueCatStatus.html')
    except Exception as e:
        return(str(e))


@app.route('/catFollowUp',methods=['GET','POST'])
def catFollowUp():
    print ("cat follow up")

    try:
        catName = request.form['catName']
        humanName = request.form['fullName']
        followUp = request.form['catFollowUp']
        print(catName,humanName)
        con = sqlite3.connect("catAdopt.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("update applications set followUp='followUp' where (catName='catName') and (fullName='humanName')")
        rows = cur.fetchall();
        con.commit()
        print ("adjusted follow up")
        return redirect('/rescueCatStatus.html')
    except Exception as e:
        return(str(e))

   

@app.route('/searchCatsPage')
def searchCatsPage():
    adoptTitle = "Cat Adoption"
    con = sqlite3.connect("catAdopt.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT DISTINCT trait1 from cats where adopted='no' LIMIT 5") #need to randomize
    rows = cur.fetchall(); 
    return render_template('searchCatsPage.html',rows=rows,adoptTitle=adoptTitle)


@app.route('/searchTraitResult', methods=['GET','POST'])
def searchTraitResult():
    if request.method =="POST":
        adoptTitle = "Cat Adoption"
        con2 = sqlite3.connect("catAdopt.db")
        con2.row_factory = sqlite3.Row
        cur2 = con2.cursor()
        searchTerm = request.form['searchTrait']
        print (searchTerm)
        #print (searchTermWentThrough)
        #cur2.execute("SELECT * FROM cats WHERE adopted='no' GROUP BY age, name HAVING (trait1='searchTerm')")
        #cur2.execute("SELECT * FROM cats WHERE adopted='no' GROUP BY age, name HAVING (trait1=searchTerm) or (trait2=searchTerm) or (trait3=searchTerm)")
    #print (queryWentThrough)
    cur2.execute("SELECT * FROM cats WHERE (((trait1='searchTerm') OR (trait2='searchTerm') OR (trait3='searchTerm')) AND adopted='no') ORDER BY rowid DESC")
    print ("queryWentThrough")
    rows2 = cur2.fetchall(); 
    print ("fetchWentThrough")
    return render_template('searchTraitResult.html',rows2=rows2,adoptTitle=adoptTitle)


if __name__ == '__main__':
	app.run()