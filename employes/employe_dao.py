import database
# importation pour le test dans init.py
#from employe import Employe
# importation pour l'exterieur du package
from employes.employe import Employe

class EmployeDao:
    connexion = database.connection_db()
    cursor = connexion.cursor()

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM employe"
        try:
            EmployeDao.cursor.execute(sql)
            employes = EmployeDao.cursor.fetchall()
            message = 'success'
        except Exception as error:
            print(error)
            employes = []
            message = 'Erreur de récupération des données !' 

        return (message, employes)    
    
    @classmethod
    def add(cls, employe: Employe):
        sql = "INSERT INTO employe(nom, prenom, matricule, fonction, departement) VALUES (%s, %s, %s, %s, %s)" 
        params = (employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement)
        try:
            EmployeDao.cursor.execute(sql, params)
            EmployeDao.connexion.commit()
            message = "success"
        except Exception as error:
            message = "failure"
        return message
    
    @classmethod
    def get_one(cls, matricule):
        sql = "SELECT * FROM employe WERE matricule=%s"
        try:
            EmployeDao.cursor.execute(sql, (matricule,))
            message = 'success'
            employe = EmployeDao.cursor.fetchone()
        except Exception as error:
            message = 'failure'
            employe = ()
            
        return (message, employe)
    
#employe = Employe('Motin-ye', 'Armel', 'MA0025', 'Pentester', 'IT')  
#print(employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement) 
      