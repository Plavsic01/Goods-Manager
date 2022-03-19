import os
from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(12).hex()

roba = []

@app.route("/")
def home():
    return render_template("index.html",roba=roba)

@app.route("/dodaj",methods=["GET","POST"])
def dodaj_robu():
    if request.method == "POST":
        proizvod = dict(request.form)
        for r in roba:
            if proizvod['id'] == r['id']:
                flash("Error Occured! ID already exists. Choose Another ID.")
                return redirect(url_for('dodaj_robu'))
        roba.append(proizvod)
        return redirect(url_for('home'))
    return render_template("dodaj_forma.html")

@app.route("/prikazi/<int:id>")
def prikazi(id):
    proizvod_id = id - 1
    proizvod = roba[proizvod_id]
    return render_template("prikaz.html",proizvod=proizvod)

@app.route("/izmeni/<int:id>",methods=["GET","POST"])
def izmeni(id):
    proizvod_id = id - 1
    proizvod = roba[proizvod_id]
    if request.method == "POST":
        novi_proizvod = dict(request.form)
        roba[proizvod_id] = novi_proizvod
        return redirect(url_for('home'))
    return render_template("izmeni_forma.html",proizvod=proizvod,id=id)

@app.route("/obrisi/<int:id>")
def obrisi(id):
    proizvod_id = id - 1
    roba.pop(proizvod_id)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()