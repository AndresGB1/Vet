from flask import Flask, render_template, redirect,url_for,request, flash
from flask.blueprints import Blueprint
from flask_mysqldb import MySQL
from rutas import rol
import os

app = Flask(__name__)
app.register_blueprint(rol.rol_api)


app.config['MYSQL_HOST'] = os.getenv('HOSTDB')
app.config['MYSQL_USER'] = os.environ.get('USERDB')
app.config['MYSQL_PASSWORD'] = os.getenv('PASSWORDDB')
app.config['MYSQL_DB'] = os.getenv('DB')

mysql = MySQL(app)

#session
app.secret_key = 'mysecretkey'
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM documento")
    data = cur.fetchall()
    mysql.connection.commit()   
    return render_template('index.html',tipos = data, roles = rol.get_rol()) 

@app.route('/add_tipo_cedula', methods=['POST'])
def tipo_documento():
    if(request.method == 'POST'):
        try:
            tipo = request.form['tipo_documento']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO documento (tipo, estado) VALUES(%s, %s)", (tipo, estado))
            mysql.connection.commit()
            flash('Document type added successfully!');
            return redirect(url_for('Index'))
        except Exception as e:
            flash('Error: ' + str(e))
            return redirect(url_for('Index'))

@app.route('/get_tipo_documento', methods=['GET'])
def get_tipo_documento():
    if(request.method == 'GET'):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM documento")
        data = cur.fetchall()
        mysql.connection.commit()
        flash('Index',tipos = data);

if __name__ == '__main__':
    app.run(port = 5000, debug = True)
