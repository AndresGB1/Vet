from flask import render_template, redirect,url_for,request, flash
from __init__ import *


#Añadiendo tipo de especie en la base de datos
@routes.route('/add_especie', methods=['POST'])
def add_mascota():
    try:
        if request.method == 'POST':
            tipo = request.form['tipo']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO especie (tipo, estado) VALUES(%s, %s)", (tipo, estado))
            mysql.connection.commit()
            flash('tipo de especie agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar la especie')
        print("No funciono ",e)
        return redirect('/')
       

