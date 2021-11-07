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
        sexo = request.form['sexo']
        usuario = request.form['usuario']
        apellido = request.form['apellido']
        password = request.form['password']
        result = crudp.getvalidusername(usuario)
        if result:
            info = "El usuario existe, debe ingresar otro"
            return redirect(url_for('insertpaciente',info=info))
        else:
            crudp.insertPaciente(nombre, sexo, usuario, apellido, password)
            info ="Usuario creado, intente ingreasar al sistema"
    return redirect(url_for('login',info=info))

def updatePaciente():

    print("Actualizacion Paciente")
    if request.method == 'POST':
        idpaciente = request.form['idpaciente']
        nombre = request.form['nombre']
        sexo = request.form['sexo']
        usuario = request.form['usuario']
        apellido = request.form['apellido']
        password = request.form['password']
   
        crudp.setUpdateData(int(idpaciente), nombre, sexo, usuario, apellido, password)
    
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
    sexo = None
    usuario = None
    apellido = None
    password = None
    ids,nombre,sexo,usuario,apellido,password =crudp.getpaciente(idusuario)
    return ids,nombre,sexo,usuario,apellido,password
    #return redirect(url_for('accesousuario', idusuario=idusuario,nombre=nombre, sexo=sexo, usuario=usuario,apellido=apellido, password=password))     

def updatePaciente2():
    idpaciente = request.form['idpaciente']
    nombre = request.form['nombre']
    sexo = request.form['sexo']
    usuario = request.form['usuario']
    apellido = request.form['apellido']
    password = request.form['password']

    crudp.setUpdateData(int(idpaciente), nombre, sexo, usuario, apellido, password)
    
    return redirect(url_for('accesousuario'))    
