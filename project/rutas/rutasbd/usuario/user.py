from flask import Flask, render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes
from .rol import *
from .documento import *
import bcrypt 

#CRUD
@routes.route('/registrar')
def usuario():
    return render_template('./usuario/usuario.html',roles = get_rol(), tdocumentos = get_tipo_documento())
    
@routes.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
    if request.method == 'POST':
        print("Entro")
        add_user(2)

@routes.route('/registrar_admin')
def usuarioAdmin():
    return render_template('./usuario/usuario.html',roles = get_rol())

@routes.route('/login', methods=['GET'])
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
def add_user(id_rol):
    try:
        if(request.method == 'POST'):
            username = request.form['username']
            if username is None or username != get_user(username):
                flash('Usuario ya existe')
            else:
                numeroDoc = request.form['numeroDoc']
                nombres = request.form['nombres']
                apellidos = request.form['appellidos']
                fecha_nacimiento = request.form['fecha_nacimiento']
                password = request.form['password']
                sexo = request.form['sexo']
                direccion = request.form['direccion']
                correo = request.form['correo']
                id_documento = request.form['tipo_documento']
                estado = True;
                cur = mysql.connection.cursor()
                cur .execute("INSERT INTO usuario (username,id_rol,id_documento, numeroDoc, nombres, apellidos, fechaNacimiento,pasword,sexo,direccion,correo,estado) VALUES(%s,%s,%s ,%s,%s, %s,%s, %s,%s, %s,%s, %s,)", (username, id_rol,id_documento,numeroDoc, nombres, apellidos, fecha_nacimiento,password,sexo,direccion,correo,estado))  
                mysql.connection.commit()
                flash('User added successfully!');
                return redirect("./usuario/usuario.html")
    except:
        flash('Error al registrar el usuario')
        return redirect(url_for('usuario'))

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
