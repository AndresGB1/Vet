from flask import render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes
from .tipo import *


#Añadiendo id_tipo nombre descripcion costo iva estado
@routes.route('/vista_admin/<string:username>/add_servicio', methods=['POST','GET'])
def add_servicio(username):
    try:
        if request.method == 'POST':
            id_tipo = request.form['id_tipo']
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            costo = request.form['costo']
            iva = request.form['iva']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO servicio (id_tipo,nombre,descripcion,costo,iva,estado) VALUES(%s,%s,%s,%s,%s,%s)",(id_tipo,nombre,descripcion,costo,iva,estado))
            mysql.connection.commit()
            flash('Servicio agregado con exito','success')
            print("Agregado prros :D ")
            return redirect('/')
        else:
            return render_template('/usuariot/add_servicio.html',username=username, tipos = get_tipos())
    except Exception as e:
        flash('Error al agregar el servicio','danger')
        print("No funciono ",e)
        return redirect('/')
       
#get_servicios
@routes.route('/vista_admin/<string:username>/get_servicios', methods=['GET'])
def get_servicios(username):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM servicio")
        servicios = cur.fetchall()
        cur.close()
        return servicios
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')
#get_servicio_id
@routes.route('/vista_admin/<string:username>/get_servicio_id/<id>', methods=['GET'])
def get_servicio_id(username,id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM servicio WHERE id=%s",(id))
        servicio = cur.fetchall()
        cur.close()
        return servicio
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')