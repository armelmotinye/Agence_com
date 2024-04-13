from flask import Flask, render_template, request
from employes.employe import Employe
from employes.employe_dao import EmployeDao

app = Flask(__name__)
app.secret_key= "cle secret"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")    
def services():
    return render_template("services.html")

@app.route("/employes")    
def employes():
    if 'username' not in session:
        return redirect(url_for('login'))
    (message, employes) = EmployeDao.get_all()
    
    return render_template("liste_employes.html", message=message,employes=employes)

@app.route("/add_employe", methods=['POST', 'GET'])
def add_employe():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form 
    print(req)
    message= None
    employe= None
    print("Methode HTTP utilisee :", request.method)
    if request.method == "POST":
        nom = req['nom']
        prenom = req['prenom']
        matricule = req['matricule']
        fonction = req['fonction']
        departement = req['departement']
        if nom =='' or prenom =='' or matricule =='' or fonction =='' or departement =='':
            message="error"
        else:
            employe = Employe(nom, prenom, matricule, fonction, departement)
            #print(employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement)
            message = EmployeDao.add(employe) 
            print(message)
    return render_template("add_employe.html", message=message, employe=employe)


@app.route("/login" , methods= ['GET', 'POST'])     
def login():
    req = request.form
    message = None
    user = None
    if request.method == "POST":
        username = req['username']
        password = req['password']
        if username == '' or password == '':
            message ='error'
            
        else:
            (message, user) = UserDao.get_one(username, password)
            if message=='success' and user != None:
                session['username'] = user[2] # mise du username dans la variable de session
                session['nom_complet'] = user[1] # mise du nom complet dans la variable de session
                return redirect(url_for('home'))
            print(message)
    return render_template("login.html", message=message, user=None)

@app.route("/logout")
def logout():
    session.clear()  # on vide les donnees de l'utilisateur dans la variable session
    return redirect(url_for('login'))