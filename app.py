import os
import secrets
from flask import Flask, session, flash, render_template, redirect, url_for, request, make_response

from flask import jsonify
from flask.globals import session
from flask_cors.decorator import cross_origin
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import defglobal as dg
# Import reglas de seguridad
import seguridad as seg

import usuarios.usuario as cp
import usuarios.apiusuarios as apiPacientes

import Publicaciones.publicacion as cm
import Publicaciones.apis as apiMedicos

def create_app():

    app = Flask(__name__)
    CORS(app)
    return app


app = create_app()


# Carpeta de subida

#app.config['UPLOAD_FOLDER'] = '/tmp'
#MyUploader = os.path.join(MYDIR + "/" + app.config['UPLOAD_FOLDER']

# Render Home page

#######################################################################
### INICIA TEMPLATES INDEX
#######################################################################
@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('index'))

@app.route('/home', methods=['GET'])
def index():
    if request.method == 'GET':
        return render_template('main/home.html')

@app.route('/mision', methods=['GET'])
def mision():
    if request.method == 'GET':
        return render_template('main/mision.html')

@app.route('/vision', methods=['GET'])
def vision():
    return render_template('main/vision.html')


@app.route('/creador', methods=['GET'])
def creador():
    return render_template('main/creador.html')


@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    return render_template('main/contacto.html')

######################### FINALIZA TEMPLATES INDEX ###################

#######################################################################
### INICIA API'S LOGIN
#######################################################################

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    #Roles
    # 1. Administrador
    # 2. Doctor
    error = None
    # "Usuario o Password o Role invalido.  Valide la informacion que ingreso"
    role = None
    usuario = None
    password = None
    result = None
    idusuario = 0
    idnombre = None
    if request.method == 'POST':
        usuario = request.form['Usuario']
        password = request.form['Pass']
        print("=========================")
        print("1. login():","usuario resquest :",usuario,", pass resquest :",password)
        print("=========================")
        result, idusuario, idnombre = seg.accesosistema(usuario,password)
        dg.idusuario = str(idusuario)
        dg.idnombre =  idnombre
        if result == 1:
            return redirect(url_for('admin'))
        if result == 2:
            return redirect(url_for('accesousuario'))
        if result == 0:
            print("Error: Usuario o Passwor no es correcto, valide de nuevo")
    print("=========================")
    print ("2. login(): result=",result, "  idusuario=",dg.idusuario," nombre=",dg.idnombre)
    print("=========================")   
    return render_template('login.html', error=error)

######################### FINALIZA API'S LOGIN ########################


#######################################################################
### INICIA API'S DE ADMIN
#######################################################################
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # recupera data y evalua si tiene para deplegar en el HTML
    
    html = request.args.get("html")
    body = request.args.get("body")
    template = 'admin/adminInfo.html'
    
    if body == '1':
       template = 'admin/adminUsuario.html' 
       print("****** BODY 1")
    if body == '2':   
        template = 'admin/adminUsuario.html'
        print("****** BODY 2")         
    if html is None:
        html = None
        print("****** BODY NONE")
    return render_template(template, html=html)


@app.route('/adminUsuario', methods=['GET', 'POST'])
def adminUsuario():
    htmlPacientes=apiPacientes.getallpaciente()

    return render_template('admin/adminUsuario.html',htmlPacientes=htmlPacientes)

@app.route('/adminMedico', methods=['GET', 'POST'])
def adminMedico():
    htmlMedicos=apiMedicos.getalldoctores()

    return render_template('admin/adminMedico.html',htmlMedicos=htmlMedicos)
    
################## FINALIZA API'S DE ADMIN ############################

#######################################################################
### INICIA API'S ADMIN DE PACIENTES
#######################################################################

@app.route("/uploadpaciente", methods=['GET','POST'])
def uploadpaciente():
    return apiPacientes.uploaderPaciente()

@app.route("/deletepaciente/<id>", methods=['GET','POST'])
def deletePaciente(id):
    return apiPacientes.deletePaciente(id)

@app.route("/updatepaciente", methods=['GET','POST'])
def updatePaciente():
    return apiPacientes.updatePaciente()

@app.route("/insertpaciente", methods=['GET','POST'])  
def insertpaciente():
    return apiPacientes.insertpaciente()
  
################### FINALIZA API'S ADMIN DE PACIENTES #######################

#######################################################################
### INICIA API'S ADMIN DE MEDICOS
#######################################################################

@app.route("/uploadmedico", methods=['POST'])
def uploadmedico():
    return apiMedicos.uploaderMedico()

@app.route("/editmedico", methods=['POST'])
def editMedico():
    html=None
    return redirect(url_for('admin', html=html))

@app.route("/deletemedico/<id>", methods=['GET','POST'])
def deleteMedico(id):
    return apiMedicos.deleteMedico(id)

@app.route("/updatemedico", methods=['GET','POST'])
def updateMedico():
    return apiMedicos.updateMedico()
    
################### FINALIZA API'S ADMIN DE MEDICOS #######################
    
#######################################################################
### INICIA API'S USUARIO DE PACIENTES
#######################################################################
@app.route('/accesousuario', methods=['GET', 'POST'])
def accesousuario():
    # recupera data y evalua si tiene para deplegar en el HTML
    html = request.args.get("html")
    body = request.args.get("body")
    
    template = 'paciente/pacientes.html'
    if body == '1':
       template = 'paciente/pedircita.html' 
    if body == '2':   
        template = 'paciente/vercita.html'
    if body == '3':   
        template = 'paciente/comprar.html' 
    if body == '4':   
        template = 'paciente/actualizarinfo.html' 
                 
    if html is None:
       html = None
    return render_template(template, html=html)

@app.route("/pacientepedircita",  methods=['GET', 'POST'])
def pacientepedircita():
    idusuario = dg.idusuario
    idnombre = dg.idnombre
    html=None
    return render_template('paciente/pedircita.html',html=html,idusuario=idusuario,idnombre=idnombre)

@app.route("/pacientecreacita", methods=['POST'])
def pacientecreacita():
    return apicitas.insertcita()

@app.route("/pacientevercita",  methods=['GET', 'POST'])
def pacientevercita():
    idusuario = dg.idusuario
    idnombre = dg.idnombre
    html=apicitas.getcitas(idusuario)
    return render_template('paciente/vercita.html',html=html,idusuario=idusuario,idnombre=idnombre)

@app.route("/pacientecomprar",  methods=['GET', 'POST'])
def pacientecomprar():
    idusuario = dg.idusuario
    idnombre = dg.idnombre
    html=None
    return render_template('paciente/comprar.html',html=html,idusuario=idusuario,idnombre=idnombre)

@app.route("/farmacia",  methods=['GET', 'POST'])
def farmacia():
    html=None
    return render_template('paciente/farmacia.html')

@app.route("/cart",  methods=['GET', 'POST'])
def cart():
    html=None
    return render_template('paciente/cart.html')

@app.route("/actualizarusuario",  methods=['GET', 'POST'])
def actualizarusuario():
    idusuario = dg.idusuario
    nombre = None
    apellido = None
    fecha = None
    sexo = None
    usuario = None
    password = None
    idusuario,nombre,apellido,fecha,sexo,usuario,password, = apiPacientes.getpaciente(idusuario)
    return render_template('paciente/actualizarinfo.html',idusuario=idusuario,nombre=nombre,apellido=apellido,fecha=fecha, sexo=sexo, usuario=usuario, password=password)

@app.route("/updatepaciente2", methods=['GET','POST'])
def updatePaciente2():
    return apiPacientes.updatePaciente2()

################### FINALIZA API'S USUARIO DE PACIENTES ###############    


#######################################################################
### INICIA API'S USUARIO DE ENFERMERAS
#######################################################################

@app.route('/accesenfermeras', methods=['GET', 'POST'])
def accesoenfermeras():
    # recupera data y evalua si tiene para deplegar en el HTML
    html = request.args.get("html")
    body = request.args.get("body")
    
    template = 'enfermera/enfermera.html'
    if body == '1':
       template = 'enfermera/citapendiente.html' 
    if body == '2':   
        template = 'enfermera/citaaceptada.html'
    if body == '3':   
        template = 'enfermera/generarfactura.html' 
    if body == '4':   
        template = 'enfermera/actualizarinfo.html' 
    if html is None:
       html = "No hay datos"
    return render_template(template, html=html)

    #Render cita pendiente
@app.route('/citapendiente', methods=['GET', 'POST'])
def citapendiente():
    idusuario = dg.idusuario
    idnombre = dg.idnombre
    estado = 1
    html=apicitas.getcitasporestado(estado)
    doctors = dg.gMedicos
    return render_template('enfermera/citapendiente.html',html=html,idusuario=idusuario,idnombre=idnombre, doctors=doctors)

@app.route('/citapendientes', methods=['GET', 'POST'])
def citapendientes():
    idusuario = dg.idusuario
    idnombre = dg.idnombre
    estado = 1
    html=apicitas.getcitasporestado(estado)
    doctors = dg.gMedicos
    return render_template('doctores/citapendiente.html',html=html,idusuario=idusuario,idnombre=idnombre, doctors=doctors)

@app.route('/citaupdateestado', methods=['GET','POST'])
def citaupdateestado():
    idcita = None
    idusuario = None
    nombre = None
    motivo = None
    fecha = None
    hora = None
    estado = None
    iddoctor = None
    if request.method == 'POST':
        idcita = request.form['txtIdCita']
        idusuario = request.form['txtIdPaciente']
        nombre = request.form['txtNombre']
        motivo = request.form['txtMotivo']
        fecha = request.form['txtFecha']
        hora = request.form['txtHora']
        estado = request.form['cbestado']
        iddoctor = request.form['cbdoctor']
        print ("Recibio estado web:",estado)
    return apicitas.updatecita(idcita,idusuario,nombre,motivo,fecha,hora,estado,iddoctor)

        #Render cita aceptada
@app.route('/citaaceptada', methods=['GET', 'POST'])
def citaaceptada():
    idusuario = dg.idusuario
    idnombre = dg.idnombre
    estado = 2
    
    html=apicitas.getcitasporestado(estado)
    print ("html aceptas",html)
    return render_template('enfermera/citaaceptada.html',html=html,idusuario=idusuario,idnombre=idnombre)

        #Render generar factura
@app.route('/generarfactura', methods=['GET', 'POST'])
def generarfactura():
    html=None
    return render_template('enfermera/facturas.html',html=html)
    

@app.route("/enfermeraactualizar",  methods=['GET', 'POST'])
def enfermeraactualizar():
    idusuario = dg.idusuario
    nombre = None
    apellido = None
    fecha = None
    sexo = None
    usuario = None
    password = None
    idusuario,nombre,apellido,fecha,sexo,usuario,password = apiEnfermeras.getenfermera(idusuario)
    return render_template('enfermera/actualizarinfoE.html',idusuario=idusuario,nombre=nombre,apellido=apellido,fecha=fecha, sexo=sexo, usuario=usuario, password=password)

@app.route("/updateenfermera2", methods=['GET','POST'])
def updateEnfermera2():
    return apiEnfermeras.updateEnfermera2()    

################### FINALIZA API'S USUARIO DE ENFERMERAS ###############    

#######################################################################
### INICIA API'S USUARIO DE DOCTORES
#######################################################################


@app.route('/accesomedicos', methods=['GET', 'POST'])
def accesomedicos():
    # recupera data y evalua si tiene para deplegar en el HTML
    html = request.args.get("html")
    body = request.args.get("body")
    template = 'doctores/doctor.html'
    if body == '1':
       template = 'doctores/citaDocPendiente.html' 
    if body == '2':   
        template = 'doctores/recetas.html'
    if body == '3':   
        template = 'enfermera/actualizarinfo.html' 
    if html is None:
       html = "No hay datos"
    return render_template(template, html=html)

@app.route('/citaspendientes', methods=['GET', 'POST'])
def citaDocPendiente():
    html=None
    return render_template('doctores/citaDocPendiente.html',html=html)

@app.route('/recetas', methods=['GET', 'POST'])
def recetas():
    html=None
    return render_template('doctores/recetas.html',html=html)


@app.route("/doctoractualizar",  methods=['GET', 'POST'])
def actualizardoctor():
    idusuario = dg.idusuario
    nombre = None
    apellido = None
    fecha = None
    sexo = None
    usuario = None
    password = None
    especialidad = None
    idusuario,nombre,apellido,fecha,sexo,usuario,password, especialidad = apiMedicos.getdoctor(idusuario)
    return render_template('doctores/actualizarinfoD.html',idusuario=idusuario,nombre=nombre,apellido=apellido,fecha=fecha, sexo=sexo, usuario=usuario, password=password,especialidad=especialidad)

@app.route("/updatedoctor2", methods=['GET','POST'])
def updateDoctor2():
    return apiMedicos.updateDoctor2()


################### FINALIZA API'S USUARIO DE DOCTORES ###############    


#######################################################################
### INICIA API'S REGISTRO
#######################################################################

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    # recupera data y evalua si tiene para deplegar en el HTML
    html = request.args.get("html")
    body = request.args.get("body")
    template = 'main/registro.html'
    
    return render_template(template, html=html)


################### FINALIZA API'S USUARIO DE REGISTRO ###############    

if __name__ == '__main__':
    secret = secrets.token_urlsafe(32)
    app.secret_key = secret
    app.config['SESSION_TYPE'] = 'redis'
    app.config.from_object(__name__)
    
    
    app.run(debug=True)
