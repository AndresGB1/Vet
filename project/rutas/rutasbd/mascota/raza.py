from flask import render_template, redirect,url_for,request, flash
from __init__ import *


#Añadiendo una raza dentro de una especie en la base de datos
@routes.route('/especie/<id>/add_raza', methods=['POST'])
def add_mascota(id):
    try:
        if request.method == 'POST':
            raza = request.form['raza']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO raza (id_especie,raza, estado) VALUES(%s, %s)", (id,raza, estado))
            mysql.connection.commit()
            flash('Nombre agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el Nombre')
        print("No funciono ",e)
        return redirect('/')
       
