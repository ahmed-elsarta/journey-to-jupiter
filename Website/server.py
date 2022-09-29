#from crypt import methods
from distutils.log import debug
import email
from email import message
from time import strptime
from time import mktime
from webbrowser import Elinks
import pandas as pd
from datetime import datetime
from datetime import timedelta
from genericpath import exists
from unittest import result
from flask import Flask, flash, redirect, render_template,request,session,url_for
from pymysql import NULL
# from sqlalchemy import false
# from flask_mysqldb import MySQL
import mysql.connector
import re
import os
import secrets

app = Flask(__name__)

hazards = [0.2,0.4,0.6,0.8]
organismsForGravity = {
    'human': 4.8*hazards[0],
    'mice': 4*hazards[0],
    'rat': 3.5*hazards[0]
}
organismsForRadiation = {
    'dr': 2.4*hazards[1],
    'tard':2.1*hazards[1],
    'human':1.85*hazards[1]
}
organismsForDna = {
    'tard' : 1.55 * hazards[2],
    'nmr': 1.3* hazards[2],
    'mice':1.1* hazards[2]
}
organismsForeye = {
    'rbs': 1.2* hazards[3],
    'human':1* hazards[3],
    'eagle':0.8* hazards[3]
}
probabilities  = []
for keyG,valG in organismsForGravity.items():
    for keyR,valR in organismsForRadiation.items():
        for keyD,valD in organismsForDna.items():
            for keyE,valE in organismsForeye.items():
                probabilities.append(valG * valR * valD * valE)


# ----------------------------------------------------------------------------index-----------------------------------------------------------
@app.route('/')
@app.route('/home',methods=["GET","POST"])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/info')
def info():
    return render_template('space-info.html')

@app.route('/mainMenu')
def mainMenu():
    return render_template('main-menu.html')

@app.route('/mainMenu/GO',methods=['GET','POST'])
def GO():
    attr1 = float(request.form['attr1'])*hazards[0]
    attr2 = float(request.form['attr2'])*hazards[1]
    attr3 = float(request.form['attr3'])*hazards[2]
    attr4 = float(request.form['attr4'])*hazards[3]
    destination = attr1 * attr2 * attr3 * attr4
    print(destination)
    
    if(destination > 0.82):
        scenario = 6
    elif destination > 0.6:
        scenario = 5
    elif destination > 0.5:
        scenario = 4
    elif destination > 0.4:
        scenario = 3
    elif destination > 0.3:
        scenario = 2
    elif destination > 0.2:
        scenario = 1
    return render_template('scenarios.html',destination = destination,scenario = scenario,attr1 = float(request.form['attr1']),attr2 = float(request.form['attr2'])
                           ,attr3 = float(request.form['attr3']),attr4 = float(request.form['attr4']))
    

if __name__ == '__main__':
    app.run(debug = True)
