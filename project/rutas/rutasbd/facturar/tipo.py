from flask import render_template, redirect,url_for,request, flash
from __init__ import *


#Añadiendo tipo de servicio a la base de datos
@routes.route('/tipo', methods=['POST'])
def add_mascota():
    try:
        if request.method == 'POST':
            tipo = request.form['tipo']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO color (tipo, estado) VALUES(%s, %s)", (tipo, estado))
            mysql.connection.commit()
            flash('Tipo de servicio agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el tipo de servicio')
        print("No funciono ",e)
        return redirect('/')
       
