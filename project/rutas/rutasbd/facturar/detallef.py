from flask import render_template, redirect,url_for,request, flash
from __init__ import *


#Añadiendo id_factura id_servicio a los detalles de la factura
@routes.route('/admin/<id>/mascota/add_color', methods=['POST'])
def add_detalle_factura():
    try:
        if request.method == 'POST':
            id_factura = request.form['id_factura']
            id_servicio = request.form['id_factura']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO detalle_factura(id_factura,id_servicio,estado) VALUES (%s,%s,%s)",(id_factura,id_servicio,estado))
            mysql.connection.commit()
            flash('Servicio agregado a la factura','success')
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el servicio','danger')
        print("No funciono ",e)
        return redirect('/')