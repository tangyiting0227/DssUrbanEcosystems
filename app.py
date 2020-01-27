# back-end related libaries
from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from functools import wraps
from collections import Counter
# database related libaries
import sqlite3
from flask_sqlalchemy import SQLAlchemy # communicate to SQLite
# system related libaries
from datetime import datetime
import numpy
import os # communicate to operation system


# set-up
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig') # define server
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # connect database
test_program = True

from models import *

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'worker_id' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('rolechoose'))
    return wrap


#@app.route('/')
#def home_page():
#    greet = "Hello Yiting"
#    return render_template("index.html", greeting=greet)
#
#@app.route('/download/') # example of sending info from backend to frontend
#def download_page():
#    name = "kevin"
#    return render_template("download.html", current_user=name)
#
#@app.route('/oops/') # example of redirect page
#def oops():
#    return redirect(url_for('download_page'), code=307)
#
## example of sending info from frontend to backend in two steps
#@app.route('/data-transfer/') # info input page
#def datatransfer():
##    print("dubug2")
##    nm = form.args.get("nm", type=str)
##    print(nm)
#    return render_template("data-transfer.html")
#
#@app.route('/password/', methods=['POST']) # info transfer page (invisible to user)
#def password():
##    pwd = request.args.get('pw', type=str)
##    nmd = request.args.get('nm', type=str)
##    print("dubug1")
##    print(pwd)
##    print(nmd)
#    print("dubug2")
#    usn = request.form['username']
#    psw = request.form['passw']
#    print(usn)
#    print(psw)
#    return render_template("index.html")
#


#@app.route('/greeting/') # example of sending info from backend to frontend
#def greeting():
#    username = "Yiting"
#    return render_template("greeting.html", current_user=username)

@app.route('/link/')
def link():
    return render_template("link.html")

@app.route('/citybuzz/')
def citybuzz():
    return render_template("citybuzz.html")

@app.route('/rolechoose/')
def rolechoose():
    return render_template("rolechoose.html")

@app.route('/raspberrypi/')
def raspberrypi():
    return render_template("raspberrypi.html")

@app.route('/choosebee/')
def choosebee():
    return render_template("choosebee.html")

@app.route('/quiz/')
def quiz():
    return render_template("quiz.html")

@app.route('/index/')
def index():
    return render_template("index.html")

@app.route('/beestatus/')
def beestatus():
    img_name = session["img_name"].split(".")[0]
    return render_template("beestatus.html", img_name=img_name)

@app.route('/citizenlogin/') # info input page
def citizenlogin():
    return render_template("citizenlogin.html")

@app.route('/basestructure/')
def basestructure():
    return render_template("basestructure.html")

@app.route('/citizenachievement/')
def citizenachievement():
    return render_template("citizenachievement.html")

@app.route('/artificialflowermap/')
def artificialflowermap():
    img_name = session["img_name"].split(".")[0]
    return render_template("artificialflowermap.html",img_name=img_name)

@app.route('/citizenuserinfo', methods=['POST'])
def citizenuserinfo():
    current_time = datetime.now()
    name = request.form['username']
    session["username"] = name
    email = request.form['email']
    password = request.form['password']
    db.session.add(Registration(name, email, current_time, password)) #save
    db.session.commit() # confirm
    return render_template("choosebee.html", current_user=name)

# example of sending info from frontend to backend in two steps
@app.route('/gardenerlogin/') # info input page
def gardenerlogin():
    return render_template("gardenerlogin.html")

@app.route('/userinfo', methods=['POST'])
def userinfo():
    current_time = datetime.now()
    name = request.form['username']
    name = "admin"
    email = request.form['email']
    password = request.form['password']
#    db.session.add(Registration(name, email, current_time, password)) #save
#    db.session.commit() # confirm
    return render_template("ArtificialFlowerDoc.html", current_user="admin")

@app.route('/ArtificialFlowerDoc/')
def ArtificialFlowerDoc():
    return render_template("ArtificialFlowerDoc.html")

@app.route('/beedatatransfer/')
def beedatatransfer():
    img_name = request.args.get("img_name", 0, type=str)
    session["img_name"] = img_name
    return jsonify("success")

@app.route('/cameradatatransfer/')
def cameradatatransfer():
    current_time = datetime.now()
    p_Bee = request.args.get("p_Bee", 0, type=str)
    print(p_Bee)
    db.session.add(Prediction("admin", p_Bee, current_time))
    db.session.commit() # confirm
    return jsonify("success")

@app.route('/beeupdate/')
def beeupdate():
    lateDetection = Prediction.query.\
                        filter(Prediction.userID=="admin").\
                        all()
    
    beeTime = []
    for item in lateDetection:
        beeTime.append(item.time)
    
    beePass = False;
    if beeTime:
        lateDetection = beeTime[-1]
#        print(lateDetection)
        beeCount = len(beeTime)
        timeDiff = (datetime.now() - lateDetection).total_seconds()
        if timeDiff < 2.5: # This number has to bigger than but as close as possible to the refreshing frequency in the javascript on the page of ArtificialFlowerDoc.html
            beePass = True;
        else:
            beePass = False;
    else:
        beePass = False;
        beeCount = 0
    return jsonify({"beePass":beePass, "beeCount":beeCount})

@app.route('/flowercollection/')
def flowercollection():
    flower = request.args.get("flower", 0, type=str)
    collectiontype = request.args.get("collectiontype", 0, type=str)
    print(flower)
    print(collectiontype)
    db.session.add(Collection(session['username'], flower, collectiontype))
    db.session.commit() # confirm
    return jsonify("seccess")

@app.route('/checkCollection/')
def checkCollection():
    clts = Collection.query.\
                        filter(Collection.userID==session['username']).\
                        all()
    
    flowers = []
    collectiontype = []
    for item in clts:
        flowers.append(item.flower)
        collectiontype.append(item.collectiontype)
    
    if flowers:
        flowers = Counter(flowers)
        collectiontype = collectiontype.count("bee")
    else:
        collectiontype = 0
    return jsonify({"flowers":flowers, "collectiontype":collectiontype})

if test_program == True:
    if __name__ == '__main__':
        app.run()
        


# examples of reading data from database

# select rows 
#    whatever = []
#    whatever = Registration.query.filter(Registration.userID=="Yiting").all()

# select colomns 
#    whatever = []
#    whatever = Registration.query.with_entities(password).all()

# select colomns and rows 
#    whatever = []
#    whatever = Registration.query.\
#    filter(Registration.userID=="Yiting").\
#    with_entities(password).\
#    all()