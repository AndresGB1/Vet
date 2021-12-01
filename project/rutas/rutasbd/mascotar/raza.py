from flask import render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes
from .especie import *

#Añadiendo una raza dentro de una especie en la base de datos
@routes.route('/especie/<id>/add_raza', methods=['POST'])
def add_especie(id):
    try:
        if request.method == 'POST':
            raza = request.form['raza']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO raza (id_especie,raza, estado) VALUES(%s, %s)", (id,raza, estado))
            mysql.connection.commit()
            flash('Nombre agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el Nombre')
        print("No funciono ",e)
        return redirect('/')

#get_all_razas
@routes.route('/get_razas', methods=['GET'])
def get_all_razas():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM raza")
        razas = cur.fetchall()
        return razas
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')
#get_raza
@routes.route('/especie/<id>/get_razas', methods=['GET'])
def get_razas(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM raza WHERE id_especie = %s", (id))
        razas = cur.fetchall()
        cur.close()
        return razas
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')
       
#get_raza_id
@routes.route('/especie/<id>/get_raza_id', methods=['GET'])
def get_raza_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM raza WHERE id_raza = %s", (id))
    raza = cur.fetchall()
    cur.close()
    return raza