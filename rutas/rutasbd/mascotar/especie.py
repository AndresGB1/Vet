from flask import render_template, redirect,url_for,request, flash
from .. import mysql
from .. import routes


#Añadiendo tipo de especie en la base de datos
@routes.route('/add_especie', methods=['POST'])
def add_mascota():
    try:
        if request.method == 'POST':
            tipo = request.form['tipo']
            estado = True
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO especie (tipo, estado) VALUES(%s, %s)", (tipo, estado))
            mysql.connection.commit()
            flash('tipo de especie agregado correctamente')
            print("Agregado prros :D ")
            return redirect('/')
    except Exception as e:
        flash('Error al agregar la especie')
        print("No funciono ",e)
        return redirect('/')
       
#get_especies
@routes.route('/get_especies', methods=['GET'])
def get_especies():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM especie")
    especies = cur.fetchall()
    cur.close()
    return especies

#get_especies_id
@routes.route('/get_especies_id/<id>', methods=['GET'])
def get_especies_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM especie WHERE id=%s", (id))
    especies = cur.fetchall()
    cur.close()
    return render_template('especie.html', especies=especies)