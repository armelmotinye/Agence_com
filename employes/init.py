from  employe_dao import EmployeDao
#from employe import Employe
from employe import Employe
(message, Employe) = EmployeDao.get_all()

print(message, Employe)

#employe = Employe('Motin-ye', 'Armel', 'MA0025', 'Pentester', 'IT')
#print(employe.nom)
#message = EmployeDao.add(employe)
#print(message)

#(message, employe) = EmployeDao.get_one('AM0025')

#print((message, employe))



