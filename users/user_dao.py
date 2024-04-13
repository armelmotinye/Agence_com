#import for test in my file init
from user import User

#import pour l'exterieur du package users
#from users.user import User

import database

class UsersDao:
    connexion = database.connection_db()
    cursor = connexion.cursor()
    
    @classmethod
    def get_one(cls, username, password):
        sql = "SELECT * FROM user WHERE username=%s AND password=%s"
        try:
            UserDao.cursor.execute(sql, (username, password))
            user = UserDao.cursor.fetchone()
            message = 'success'
        except Exception as error:
            message= 'failure'
            user = ()
        return (message, user)