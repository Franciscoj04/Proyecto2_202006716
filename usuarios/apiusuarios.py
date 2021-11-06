import os

from flask import Flask, flash, render_template, redirect, url_for, request
from flask import jsonify
from flask_cors.decorator import cross_origin
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

import usuarios.usuario as classP
import usuarios.leerarchivo as rd
import usuarios.crudusuario as crudp
import defglobal as dg

# Carga el archivo de Usuarios
def uploaderPaciente():
    
    if request.method == 'POST':
        html = None
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        # Nombres CSV y Json
        fcsv = os.path.join(dg.MYDIR,filename)
        print ("++++++   archivos subir a Heroku",fcsv)
        # Guardamos el archivo en el directorio "CargadeArchivos"
        if f:
            f.save(fcsv)
            html = rd.getFilePaciente(fcsv)

        else:    
            pass
            print ("***** RENDER Body 1")
        body = '1'
        print ("+++++++++ url_for")
        return redirect(url_for('adminUsuario'))
        #return "ok"
        


# Render creador page
def insertpaciente():
    info = None
    print("++++++ Insert paciente")
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']
        sexo = request.form['sexo']
        usuario = request.form['usuario']
        password = request.form['password']
        result = crudp.getvalidusername(usuario)
        if result:
            info = "El usuario existe, debe ingresar otro"
            return redirect(url_for('insertpaciente',info=info))
        else:
            crudp.insertPaciente(nombre, apellido, fecha, sexo, usuario, password)
            info ="Usuario creado, intente ingreasar al sistema"
    return redirect(url_for('login',info=info))

def updatePaciente():

    print("Actualizacion Paciente")
    if request.method == 'POST':
        idpaciente = request.form['idpaciente']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        fecha = request.form['fecha']
        sexo = request.form['sexo']
        usuario = request.form['usuario']
        password = request.form['password']
   
        crudp.setUpdateData(int(idpaciente), nombre, apellido, fecha, sexo, usuario, password)
    
    html=crudp.listToHTML()
    
    body = '1'
    
    return redirect(url_for('adminUsuario'))

def deletePaciente(id):
    crudp.deleteData(id)
    html = crudp.listToHTML()
    body = '1'
    return redirect(url_for('adminUsuario'))

def getallpaciente():
    html = crudp.listToHTML()
    return html    

def getpaciente(idusuario):
    ids = None
    nombre = None
    apellido = None
    fecha = None
    sexo = None
    usuario = None
    password = None
    ids,nombre,apellido,fecha,sexo,usuario,password =crudp.getpaciente(idusuario)
    return ids,nombre,apellido,fecha,sexo,usuario,password
    #return redirect(url_for('accesousuario', idusuario=idusuario,nombre=nombre,apellido=apellido,fecha=fecha, sexo=sexo, usuario=usuario, password=password))     

def updatePaciente2():
    idpaciente = request.form['idpaciente']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    fecha = request.form['fecha']
    sexo = request.form['sexo']
    usuario = request.form['usuario']
    password = request.form['password']

    crudp.setUpdateData(int(idpaciente), nombre, apellido, fecha, sexo, usuario, password)
    
    return redirect(url_for('accesousuario'))    
