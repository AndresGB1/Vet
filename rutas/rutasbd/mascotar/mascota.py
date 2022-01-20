from flask import Flask, render_template, redirect,url_for,request, flash
from .color import *
from .raza import *


       
@routes.route('/cliente/<string:username>/nueva_mascota', methods=['GET'])
def nueva_mascota(username):
    return render_template('usuariot/add_mascotas.html', name=username, colores = get_colores(), especies=get_especies(), razas=get_all_razas())

@routes.route('/cliente/<string:username>/add_mascota', methods=['POST'])
def add_mascotau(username): 
    if request.method == 'POST':
        try:
            id_usuario = request.form['user_name']
            nombre = request.form['nombre']
            sexo = request.form['sexo']
            peso = request.form['peso']
            fechaNacimiento = request.form['fecha_nacimiento']
            id_raza = request.form['id_raza']
            id_color = request.form['id_color']
            estado = True
            cur = mysql.connection.cursor()
            cur .execute("INSERT INTO mascota (id_usuario, id_raza, id_color, nombre, sexo, peso, fecha_nacimiento, estado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (id_usuario, id_raza, id_color, nombre, sexo, peso, fechaNacimiento, estado))
            mysql.connection.commit()
            flash('Mascota added successfully!')
            return redirect('/cliente/'+username+'/nueva_mascota') 
        except Exception as e:
            print('Error: ' + str(e))
            return redirect('/cliente/'+username+'/nueva_mascota')

@routes.route('/cliente/<string:username>/ver_mascotas', methods=['GET'])
def ver_mascotau(username):
    if request.method == 'GET':
        return render_template('usuariot/mascotas.html', name=username, mascotas=get_mascotas(username))


#get
@routes.route('/user/<string:username>/get_mascotas', methods=['GET'])
def get_mascotas(username):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mascota WHERE id_usuario = %s", [username])
    data = cur.fetchall()
    cur.close()
    return data

#get_by_id
@routes.route('/cliente/<string:username>/get_mascota/<string:id>', methods=['GET'])
def get_mascota(username, id):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        cur.execute("SELECT m.* FROM mascota m usuario u WHERE u.id_usuario = %s AND id_mascota = %s", (username, id))
        data = cur.fetchall()
        return render_template('mascota/mascota.html', mascotas = data)
    

#delete_by_id
@routes.route('/cliente/<string:username>/delete_mascota/<id>', methods=['GET', 'POST'])
def delete_mascota(username, id):
    cur = mysql.connection.cursor()
    cur.execute('update mascota SET estado = false WHERE id = %s', [id])
    mysql.connection.commit()
    cur.close()
    return redirect('/cliente/'+username+'/ver_mascotas')