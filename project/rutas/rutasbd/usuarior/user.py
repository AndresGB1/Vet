from flask import Flask, render_template, redirect,url_for,request, flash
from .. import routes
from .. import mysql
from .rol import *
from .documento import *
from ..mascotar.mascota import *
import hashlib

#CRUD
@routes.route('/registrar')
def usuario():
    return render_template('/usuariot/usuario.html',roles = [[2,"Cliente",1]], tdocumentos = get_tipo_documento())

@routes.route('/vista_cliente/<string:username>')
def vista_cliente(username):
    return render_template('/usuariot/cliente.html', name = username, mascotas = get_mascotas(username))

@routes.route('/vista_admin/<string:username>')
def vista_admin(username):
    return render_template('./usuariot/admin.html', name = username)
    
@routes.route('/vista_veterinario/<string:username>')
def vista_veterinario(username):
    return render_template('./usuariot/veterinario.html', name = username)

@routes.route('/registrar_usuario', methods=['POST'])
def registrar_usuario():
   if(request.method == 'POST'):
            username = request.form['username']
            data = get_user(username)
            if(len(data) == 0 ):
                numeroDoc = request.form['numeroDoc']
                numeroDoc = str(numeroDoc)
                nombres = request.form['nombres']
                apellidos = request.form['apellidos']
                fecha_nacimiento = request.form['date']
                password = request.form['password']
                password = hashlib.sha1(password.encode('utf-8')).hexdigest()
                sexo = request.form['sexo']
                direccion = request.form['direccion']
                correo = request.form['correo']
                id_documento = request.form['tipo_documento']
                id_rol = request.form['id_rol']
                estado = True;
                cur = mysql.connection.cursor()
                cur .execute("INSERT INTO usuario (username,id_rol,id_documento, numeroDoc, nombres, apellidos, fecha_nacimiento,pasword,sexo,direccion,correo,estado) VALUES(%s,%s,%s ,%s,%s, %s,%s, %s,%s, %s,%s, %s)", (username, id_rol,id_documento,numeroDoc, nombres, apellidos, fecha_nacimiento,password,sexo,direccion,correo,estado))  
                mysql.connection.commit()
                flash('User added successfully!')
                return redirect('/vista_cliente')
            else:
                return redirect('/registrar')
                #return render_template('./usuario/usuario.html',roles = [[2,"Cliente",1]], tdocumentos = get_tipo_documento())

@routes.route('/registrar_admin')
def usuarioAdmin():
    return render_template('./usuario/usuario.html',roles = get_rol())

@routes.route('/login', methods=['POST'])
def login():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            hashed = hashlib.sha1(password.encode('utf-8')).hexdigest()
            data = get_user(username)
            if(len(data) == 0 ):
                print("No existe el usuario")
                flash('Usuario no existe')
                return redirect('/')
            else:                
                if data[0][7] == hashed:
                    flash('Logueado exitosamente')
                    if data[0][1] == 2:
                        return redirect("./vista_cliente/"+username)
                    if data[0][1] == 3:
                        return redirect("./vista_veterinario"+username)
                    if data[0][1] == 1:
                        return redirect("./vista_admin/"+username)
            flash('Contraseña incorrecta')
            return redirect('/')
        else:
            return redirect('/')
            
    except:
        return redirect('/')

@routes.route('/user/<string:username>')
def get_user(username):
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE username =  "{0}"'.format(username))
        data = cur.fetchall()
        cur.close()
        return data
    except Exception as e:
        return []        

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
