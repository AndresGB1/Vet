from flask import render_template, redirect,url_for,request, flash
from database import mysql
from .. import routes


#Añadiendo tipo de servicio a la base de datos
@routes.route('/tipo', methods=['POST'])
def add_tipo():
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
       
#get_tipo
@routes.route('/tipos', methods=['GET'])
def get_tipos():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tipo")
        tipos = cur.fetchall()
        print("Tipos de servicio: ", tipos)
        return tipos
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')
#get_tipo_id
@routes.route('/tipo/<id>', methods=['GET'])
def get_tipo_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM tipo WHERE id = %s", (id))
        tipo = cur.fetchall()
        return tipo
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')