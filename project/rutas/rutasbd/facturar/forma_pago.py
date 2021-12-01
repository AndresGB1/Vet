from flask import render_template, redirect,url_for,request, flash
from __init__ import *


#Añadiendo el tipo de pago a la base de datos
@routes.route('/add_forma_pago', methods=['POST'])
def add_forma_pago():
    try:
        if request.method == 'POST':
            tipo_pago = request.form['tipo_pago']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO formapago (tipo_pago, estado) VALUES(%s, %s)", (tipo_pago, estado))
            mysql.connection.commit()
            flash('Nombre agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el Nombre')
        print("No funciono ",e)
        return redirect('/')
    