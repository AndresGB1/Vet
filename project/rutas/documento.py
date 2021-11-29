from flask import Flask, render_template, redirect,url_for,request, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
mysql = MySQL(app)

@app.route('/add_documento', methods=['POST'])
def add_documento():
    if(request.method == 'POST'):
        try:
            tipo = request.form['tipo']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO documento(tipo, estado) VALUES(%s, %s)", (tipo, estado))
            mysql.connection.commit()
            flash('Documento agregado correctamente')
            return redirect(url_for('Index'))
        except:
            flash('Error al agregar el documento')
            return redirect(url_for('Index'))
@app.route('/get_tipo_documento', methods=['POST'])
def get_tipo_documento():
    if(request.method == 'GET'):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM documento")
        data = cur.fetchall()
        mysql.connection.commit()
        flash('Index',tipos = data);
if __name__ == '__main__':
    app.run(port = 5000, debug = True)