from flask import Flask, render_template, app, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:mysql%40123@localhost:3306/services'
db=SQLAlchemy(app)

class Accomodation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brokername = db.Column(db.String(100))
    contactno = db.Column(db.Integer)

class Restaurant(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    rname=db.Column(db.String(100))
    contactno=db.Column(db.Integer)
    address=db.Column(db.String(100))
    gmaps=db.Column(db.String(100))


@app.route("/",methods=['GET'])
def getHome():
    return render_template('home.html')

@app.route("/account",methods=['GET'])
def getAcc():
    accommo=Accomodation.query.all()
    result=[{'id': acc.id, 'brokername': acc.brokername, 'contactno': acc.contactno} for acc in accommo]
    return render_template('account.html',data=result)

 

if __name__=='__main__':
    app.run(debug=True)



    