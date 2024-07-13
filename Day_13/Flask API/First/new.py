from flask import Flask, render_template, app

app=Flask(__name__)

@app.route("/",methods=['GET'])
def getHome():
    return "Welcome home"

@app.route("/books",methods=['GET'])
def getBooks():
    booklist=["Complete Reference python","Mastering python","Deep dive into Mysql"]
    return booklist

if __name__=='__main__':
    app.run(debug=True)