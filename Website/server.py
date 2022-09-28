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
app.secret_key = "very secret key"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="85426Mm854267890",
    database="felcode"
)
mycursor = mydb.cursor(buffered=True)

# -----------------------------------------------------------------------------index-----------------------------------------------------------
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
    attr1 = float(request.form['attr1'])
    attr2 = float(request.form['attr2'])
    attr3 = float(request.form['attr3'])
    attr4 = float(request.form['attr4'])
    
    return render_template('go.html',destination = attr1 * attr2 * attr3 * attr4)
    

if __name__ == '__main__':
    app.run(debug = True)
