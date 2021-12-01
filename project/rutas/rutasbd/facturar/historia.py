from flask import render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes


#template
@routes.route('/vista_veterinario/<string:username>/nueva_historia', methods=['GET'])
def nueva_historia(username):
    return render_template('./usuariot/add_historia.html', name = username)

#Añadiendo la historia a una mascota (id_mascota empleado fecha_creacion estado )
@routes.route('/vista_veterinario/<string:username>/add_historia', methods=['POST'])
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
            return redirect('/vista_veterinario/'+username+'/nueva_historia')
    except:
        return redirect('/vista_veterinario/'+username+'/nueva_historia')
