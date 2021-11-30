from flask import Flask, render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes
from .rol import *
import bcrypt 

#CRUD
@routes.route('/registrar')
def usuario():
    return render_template('./usuario/usuario.html',roles = get_rol())

@routes.route('/registrar_admin')
def usuarioAdmin():
    return render_template('./usuario/usuario.html',roles = get_rol())

@routes.route('/login', METHODS=['GET'])
def login():
    try:
        if request.method == 'GET':
            username = request.form['username']
            password = request.form['password']
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM usuario WHERE username = %s", (username))
            user = cur.fetchone()
            print(user)
            if user is None:
                flash('Usuario no existe')
                return redirect('/')
            else:
                if user.password == hashed:
                    if user.rol == 'cliente':
                        return redirect("./usuario/cliente")
                    if user.rol == 'veterinario':
                        return redirect("./usuario/veterinario")
                    if user.rol == 'admin':
                        return redirect("./usuario/admin")

            

            
    except:
        return redirect(url_for('rutas.login'))

@routes.route('/user/<string:id>', methods = ['GET'])
def get_user(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE username = %s', (id))
        data = cur.fetchall()
        cur.close()
        flash('Usuario encontrado')
        return render_template('./usuario/usuario.html',usuario=data[0])
    except:
        flash('Error al recuperar el usuario')
        return redirect(url_for('usuario'))

#Create
@routes.route('/add_user', methods=['POST'])
def add_user():
    if(request.method == 'POST'):
        username = request.form['username']
        numeroDoc = request.form['numeroDoc']
        nombres = request.form['nombres']
        apellidos = request.form['appellidos']
        fecha_nacimiento = request.form['fecha_nacimiento']
        password = request.form['password']
        sexo = request.form['sexo']
        direccion = request.form['direccion']
        correo = request.form['correo']
        estado = True;
        cur = mysql.connection.cursor()
        cur .execute("INSERT INTO usuario (username, numeroDoc, nombres, apellidos, fechaNacimiento,pasword,sexo,direccion,correo,estado) VALUES(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,)", (username, numeroDoc, nombres, apellidos, fecha_nacimiento,password,sexo,direccion,correo,estado))  
        mysql.connection.commit()
        flash('User added successfully!');
        return redirect(url_for('Index'))

#edit
@routes.route('/edit_user/<string:id>', methods = ['POST', 'GET'])
def get_contact_edit(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE username = %s', (id))
    data = cur.fetchall()
    cur.close()
    return render_template('edit-user.html', contact = data[0])

#edit
@routes.route('/user/update/<string:id>', methods=['POST'])
def update_user(id):
    if request.method == 'POST':
        numeroDoc = request.form['numeroDoc']
        nombres = request.form['nombres']
        apellidos = request.form['appellidos']
        fecha_nacimiento = request.form['fecha_nacimiento']
        password = request.form['password']
        sexo = request.form['sexo']
        direccion = request.form['direccion']
        correo = request.form['correo']
        estado = True;
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET numeroDoc = %s,
                nombres = %s,
                apellidos = %s
                
            WHERE id = %s
        """)
        flash('Contact Updated Successfully')
        mysql.connection.commit()
        return redirect(url_for('Index'))
