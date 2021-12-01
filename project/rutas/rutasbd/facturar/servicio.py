from flask import render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes


#Añadiendo id_tipo nombre descripcion costo iva estado
@routes.route('/add_servicio', methods=['POST'])
def add_servicio(id):
    try:
        if request.method == 'POST':
            id_tipo = request.form['id_tipo']
            nombre = request.form['nombre']
            descripcion = request.form['descripcion']
            costo = request.form['costo']
            iva = request.form['iva']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO servicio (id_tipo,nombre,descripcion,costo,iva,estado) VALUES(%s,%s,%s,%s,%s,%s)",(id,nombre,descripcion,costo,iva,estado))
            mysql.connection.commit()
            flash('Servicio agregado con exito','success')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el servicio','danger')
        print("No funciono ",e)
        return redirect('/')
       
#get_servicios
@routes.route('/get_servicios', methods=['GET'])
def get_servicios():
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
@routes.route('/get_servicio_id/<id>', methods=['GET'])
def get_servicio_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM servicio WHERE id=%s",(id))
        servicio = cur.fetchall()
        cur.close()
        return servicio
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')