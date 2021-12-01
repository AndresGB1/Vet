from flask import Flask, render_template, redirect,url_for,request, flash
from flask_mysqldb import MySQL
from .. import routes
from .. import mysql


@routes.route('/add_documento', methods=['POST'])
def add_documento():
    if(request.method == 'POST'):
        try:
            tipo = request.form['tipo']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO documento(tipo, estado) VALUES(%s, %s)", (tipo, estado))
            mysql.connection.commit()
            cur.close()
            flash('Documento agregado correctamente')
            return redirect(url_for('Index'))
        except:
            flash('Error al agregar el documento')
            return redirect(url_for('Index'))

@routes.route('/get_tipo_documento')
def get_tipo_documento():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM documento")
    data = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    print(data)
    return data