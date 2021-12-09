from flask import Flask
from flask_mysqldb import MySQL
from rutas import routes
import os


app = Flask(__name__)

#Conexión a BD con archivo .env
app.config['MYSQL_HOST'] = os.getenv('HOSTDB') #'localhost'
app.config['MYSQL_USER'] = os.environ.get('USERDB') #'usuario'
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORDDB') #'password'
app.config['MYSQL_DB'] = os.getenv('DB') #'Base de datos'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)
app.register_blueprint(routes) #Registrar las rutas


if __name__ == '__main__':
    app.run(port = 5000, debug = False)
