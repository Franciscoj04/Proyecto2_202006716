# definicion de funciones para publicaciones
###########################################
import os
import app as m
from flask import Flask, flash, render_template, redirect, url_for, request
from flask import jsonify
from flask_cors.decorator import cross_origin
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

import Publicaciones.publicacion as classM
import Publicaciones.readFiles as rd
import Publicaciones.crudpublicaciones as crudm
import defglobal as dg


# Carga el archivo de medicos
def uploaderMedico():
    
    if request.method == 'POST':
        html = None
        # obtenemos el archivo del input "archivo"
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        print ("************** 1")
        # Nombres CSV y Json
        fcsv = os.path.join(dg.MYDIR,filename)
        print ("************** 2")
        # Guardamos el archivo en el directorio "CargadeArchivos"
        if f:
            print ("************** 3")
            f.save(fcsv)
            # Retornamos una respuesta satisfactoria
            html = rd.getFileMedico(fcsv)
        else:
            print ("************** 3")
            pass
        body = '2'
        print ("************** 4")
        return redirect(url_for('adminMedico'))

# Render creador page

def updateMedico():
    id = request.form['id']
    nombre = request.form['nombre']
    sexo = request.form['sexo']
    usuario = request.form['usuario']
    apellido = request.form['apellido']
    password = request.form['password']

    crudm.setUpdateData(id, nombre, sexo, usuario, apellido, password)
    html=crudm.listToHTML()
    body = '2'
    return redirect(url_for('adminMedico'))

def deleteMedico(id):
    crudm.deleteData(id)
    html = crudm.listToHTML()
    body = '2'
    return redirect(url_for('adminMedico'))

def getalldoctores():
    html = crudm.listToHTML()
    return html    



def getdoctor(idusuario):
    ids = None
    nombre = None
    sexo = None
    usuario = None
    apellido = None
    password = None
    ids,nombre,sexo,usuario,apellido,password =crudm.getdoctor(idusuario)
    return ids,nombre,sexo,usuario,apellido,password
    #return redirect(url_for('accesousuario', idusuario=idusuario,nombre=nombre, sexo=sexo, usuario=usuario,apellido=apellido, password=password))     

def updateDoctor2():
    id = request.form['id']
    nombre = request.form['nombre']
    sexo = request.form['sexo']
    usuario = request.form['usuario']
    apellido = request.form['apellido']
    password = request.form['password']

    crudm.setUpdateData(id, nombre, sexo, usuario, apellido, password)
    
    return redirect(url_for('accesomedicos'))    
