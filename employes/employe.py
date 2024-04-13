class Employe:
    def __init__(self, nom, prenom, matricule, fonction, departement):
        self._nom = nom 
        self._prenom = prenom 
        self._matricule = matricule
        self._fonction = fonction
        self._departement = departement

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def matricule(self):
        return self._matricule

    @matricule.setter
    def matricule(self, value):
        self._matricule = value

    @property
    def fonction(self):
        return self._fonction

    @fonction.setter
    def fonction(self, value):
        self._fonction = value

    @property
    def departement(self):
        return self._departement

    @departement.setter
    def departement(self, value):
        self._departement = value

#employe = Employe('Motin-ye', 'Armel', 'MA0025', 'Pentester', 'IT')  
#print(employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement)  
