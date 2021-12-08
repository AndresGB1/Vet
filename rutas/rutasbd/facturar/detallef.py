from flask import render_template, redirect,url_for,request, flash
from .. import routes
from .. import mysql

@routes.route('/')
#Añadiendo id_factura id_servicio a los detalles de la factura
@routes.route('/admin/<username>/mascota/add_color', methods=['POST'])
def add_detalle_factura(username):
    try:
        if request.method == 'POST':
            id_factura = request.form['id_factura']
            servicios = request.form['id_servicios']
            estado = True
            for servicio in servicios:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO detalle_factura(id_factura,id_servicio,estado) VALUES (%s,%s,%s)",(id_factura,servicio,estado))
                mysql.connection.commit()
            flash('Servicio agregado a la factura','success')
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el servicio','danger')
        print("No funciono ",e)
        return redirect('/')