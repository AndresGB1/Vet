from flask import  render_template, redirect,url_for,request, flash
from flask import Blueprint
from __init__ import *
"""
Aquí se agregan los numeros de telefono que tiene un usuario
"""

#Create
@routes.route('/user/<string:id>/add_telefono', methods=['POST'])
def add_telefono():
    try:
        if request.method == 'POST':
            telefono = request.form['telefono']
            estado = True;
            if telefono == '':
                flash('El campo telefono esta vacio')
                return redirect('/')
            else:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO telefono (telefono, estado) VALUES(%s, %s)", (telefono, estado))
                mysql.connection.commit()
                flash('Telefono agregado con exito')
                return redirect('/')
    except Exception as e:
        flash('Error al agregar telefono')
        return redirect('/')