from flask import Flask, flash, redirect, render_template,request,session,url_for
# from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import pandas as pd


app = Flask(__name__)
app.secret_key = "very secret key"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="magdynasr",
    database="spaceapps"
)
mycursor = mydb.cursor(buffered=True)


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
    return render_template('info.html')

@app.route('/mainMenu', methods = ['GET', 'POST'])
def mainMenu():
    return render_template('main-menu.html')

@app.route('/mainMenu/GO',methods=['GET','POST'])
def GO():
    if request.method  == "POST":
        attr1 = float(request.form['attr1'])*hazards[0]
        attr2 = float(request.form['attr2'])*hazards[1]
        attr3 = float(request.form['attr3'])*hazards[2]
        attr4 = float(request.form['attr4'])*hazards[3]
        name = request.form['name']

        destination = attr1 * attr2 * attr3 * attr4
        print(destination)

        if(destination > 0.82):
            scenario = 6
            distance = 5050
        elif destination > 0.6:
            scenario = 5
            distance = 4400
        elif destination > 0.5:
            scenario = 4
            distance = 2900
        elif destination > 0.4:
            scenario = 3
            distance = 1200
        elif destination > 0.3:
            scenario = 2
            distance = 715
        elif destination > 0.2:
            scenario = 1
            distance = 225
        sql5 = """INSERT INTO dashboard (userName,distance) VALUES (%s,%s)"""
        val5= (name,distance)
        mycursor.execute(sql5,val5)
        mydb.commit()
        return render_template('scenario2.html',destination = destination,scenario = scenario,attr1 = float(request.form['attr1']),attr2 = float(request.form['attr2'])
                            ,attr3 = float(request.form['attr3']),attr4 = float(request.form['attr4']),distance = distance)
    else:
        return render_template('main-menu.html')

@app.route('/animals_info')
def animales_info():
    return render_template('animals-info.html')

@app.route('/space_info')
def space_info():
    return render_template('space-info.html')

@app.route('/scoreboard')
def scoreboard():
    sql = """SELECT userName,distance FROM dashboard"""
    mycursor.execute(sql,)
    result = mycursor.fetchall()
    result = pd.DataFrame(result)

    print(result)
    if not result.empty:
        result[1] = result[1].astype(int)
        result = result.sort_values(by=1,ascending = False)
        result.index = range(len(result.index))
        print(result)
    
    
    return render_template('scoreboard.html', data = result)
if __name__ == '__main__':
    app.run(debug = True)
