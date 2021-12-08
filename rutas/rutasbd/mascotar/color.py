from flask import render_template, redirect,url_for,request, flash
from .. import routes
from .. import mysql


#Añadiendo id_usuario id_raza estado id_color nombre sexo peso fechaNacimiento
@routes.route('/add_color', methods=['POST'])
def add_color():
    try:
        if request.method == 'POST':
            nombre = request.form['nombre']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO color (nombre, estado) VALUES(%s, %s)", (nombre, estado))
            mysql.connection.commit()
            flash('Nombre agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el Nombre')
        print("No funciono ",e)
        return redirect('/')
#get_colores
@routes.route('/get_colores', methods=['GET'])
def get_colores():
    try:
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM color")
            colores = cur.fetchall()
            cur.close()
            return colores
    except Exception as e:
        flash('Error al obtener los colores')
        print("No funciono ",e)
        return redirect('/')
#get_color_id
@routes.route('/get_color_id/<id>', methods=['GET'])
def get_color_id(id):
    try:
        if request.method == 'GET':
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM color WHERE id_color = %s", (id))
            color = cur.fetchall()
            cur.close()
            return color
    except Exception as e:
        flash('Error al obtener los colores')
        print("No funciono ",e)
        return redirect('/')