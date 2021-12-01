from flask import render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes


#Añadiendo el tipo de pago a la base de datos
@routes.route('/add_forma_pago', methods=['POST'])
def add_forma_pago():
    try:
        if request.method == 'POST':
            tipo_pago = request.form['tipo_pago']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO formapago (tipo_pago, estado) VALUES(%s, %s)", (tipo_pago, estado))
            mysql.connection.commit()
            flash('Nombre agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar el Nombre')
        print("No funciono ",e)
        return redirect('/')
#get_formas_pago
@routes.route('/get_formas_pago', methods=['GET'])
def get_formas_pago():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM formapago")
        formas_pago = cur.fetchall()
        cur.close()
        return formas_pago
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')
#get_formas_pago_id
@routes.route('/get_formas_pago_id/<id>', methods=['GET'])
def get_formas_pago_id(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM formapago WHERE id=%s", (id))
        formas_pago = cur.fetchall()
        cur.close()
        return formas_pago
    except Exception as e:
        print("No funciono ",e)
        return redirect('/')