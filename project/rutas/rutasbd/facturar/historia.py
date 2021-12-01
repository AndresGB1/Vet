from flask import render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes


#Añadiendo id_usuario id_raza estado id_color nombre sexo peso fechaNacimiento
@routes.route('/mascota/<id>/add_historia', methods=['POST'])
def add_mascota(id):
    try:
        if request.method == 'POST':
            nombre = request.form['nombre']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO color (id_mascota,nombre, estado) VALUES(%s, %s)", (id,nombre, estado))
            mysql.connection.commit()
            flash('Nombre agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el Nombre')
        print("No funciono ",e)
        return redirect('/')
       

#edit
@routes.route('/admin/<id>/mascota/set_color/<id>', methods = ['POST', 'GET'])
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuario WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    return render_template('edit-user.html', contact = data[0])

#edit
@routes.route('/user/update/<id>', methods=['POST'])
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
