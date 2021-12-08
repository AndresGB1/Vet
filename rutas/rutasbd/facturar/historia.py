from flask import render_template, redirect,request, flash
from .. import mysql
from .. import routes
from .factura import *


#template
@routes.route('/admin/<string:username>/nueva_historia', methods=['GET'])
def nueva_historia(username):
    return render_template('./usuariot/add_historia.html', name = username)

#Añadiendo la historia a una mascota (id_mascota empleado fecha_creacion estado )
@routes.route('/admin/<string:username>/add_historia', methods=['POST'])
def add_historia(username):
    try:
        if request.method == 'POST':
            empleado = username
            id_mascota = request.form['id_mascota']
            fecha_creacion = request.form['fecha_historia']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO historia (id_mascota,empleado, fecha_creacion, estado) VALUES (%s, %s, %s, %s)", (id_mascota,empleado, fecha_creacion, estado))
            mysql.connection.commit()
            cur.close()
            flash('Historia creada exitosamente!')
            return redirect('/admin/'+username+'/nueva_historia')
    except:
        return redirect('/admin/'+username+'/nueva_historia')
#get_historias_id
@routes.route('/admin/<string:username>/get_historia', methods=['POST'])
def get_historia_id(username):

        id = request.form['historia']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM historia WHERE id_mascota = %s', [id])
        historias = cur.fetchall()
        cur.close()
        if(len(historias) > 0):
            return render_template('/administrador/facturas_mascota.html',name=username, historias = historias[0],facturas=get_facturas() )
        flash('No existe la historia')
        return redirect('/admin/'+username+'/nueva_historia')
        flash('Historia cargada exitosamente!')


