from flask import Flask, render_template, redirect,url_for,request, flash
from .. import routes
from .. import mysql


#Añadiendo id_usuario id_raza estado id_color nombre sexo peso fechaNacimiento
@routes.route('/user/<string:id>/add_mascota', methods=['POST'])
def add_mascota(id):
    if(request.method == 'POST'):
        id_usuario = id
        id_raza = request.form['id_raza']
        id_color = request.form['id_color']
        nombre = request.form['nombre']
        sexo = request.form['sexo']
        peso = request.form['peso']
        fechaNacimiento = request.form['fechaNacimiento']
        estado = True;
        cur = mysql.connection.cursor()
        cur .execute("INSERT INTO mascota (id_usuario, id_raza, id_color, nombre, sexo, peso, fechaNacimiento, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id_usuario, id_raza, id_color, nombre, sexo, peso, fechaNacimiento, estado))
        mysql.connection.commit()
        flash('Mascota added successfully!');
        return redirect(url_for('Index'))
#get
@routes.route('/user/<string:username>/get_mascotas', methods=['GET'])
def get_mascotas(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mascota WHERE id_usuario = %s", [username])
    data = cur.fetchall()
    return render_template('usuario/mascota.html', mascotas = data)

#get_by_id
@routes.route('/user/<string:username>/get_mascota/<string:id>', methods=['GET'])
def get_mascota(username, id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mascota WHERE id_usuario = %s AND id_mascota = %s", (username, id))
    data = cur.fetchall()
    return render_template('mascota/mascota.html', mascotas = data)
