from flask import  render_template, redirect,url_for,request, flash
from flask import Blueprint
from .. import mysql
from .. import routes




#Create
@routes.route('/add_rol', methods=['POST'])
def add_rol():
    try:
        if request.method == 'POST':
            descripcion = request.form['descripcion']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO rol (descripcion, estado) VALUES(%s, %s)", (descripcion, estado))
            mysql.connection.commit()
            flash('Rol agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el rol')
        print("No funciono ",e)
        return redirect('/')

@routes.route('/get_rol', methods=['GET'])
def get_rol():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM rol")
        data = cur.fetchall()
        mysql.connection.commit()
        return data
    except:
        flash('Error al obtener los roles')
        


@routes.route('/edit_rol', methods=['POST'])
def edit_rol():
    try:
        if request.method == 'POST':
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO rol (descripcion, estado) VALUES(%s, %s)")
            mysql.connection.commit()
            flash('Rol agregado correctamente')
            return redirect(url_for('Index'))
    except Exception as e:
        flash('Error al agregar el rol')
        return redirect(url_for('Index'))