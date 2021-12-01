from flask import render_template, redirect,url_for,request, flash
from __init__ import *


#Añadiendo id_tipo nombre descripcion costo iva estado
@routes.route('/tipo_de_servicio/<id>/add_servicio', methods=['POST'])
def add_servicio(id):
    try:
        if request.method == 'POST':
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            costo = request.form['costo']
            iva = request.form['iva']
            estado = request.form['estado']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO servicio(id_tipo,nombre,descripcion,costo,iva,estado) VALUES(%s,%s,%s,%s,%s,%s)",(id,nombre,descripcion,costo,iva,estado))
            mysql.connection.commit()
            flash('Servicio agregado con exito','success')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el servicio','danger')
        print("No funciono ",e)
        return redirect('/')
       
