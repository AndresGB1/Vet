from flask import render_template, redirect,url_for,request, flash
from __init__ import *


#Añadiendo id_usuario id_raza estado id_color nombre sexo peso fechaNacimiento
@routes.route('/add_color', methods=['POST'])
def add_mascota():
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