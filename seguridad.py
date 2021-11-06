import defglobal as dg


################################################################
## La funcion accesosistema, busca en cada objeto:
##      Admin, Doctor, Enfermera o Paciente
##      si existe el usuario.  Si lo encuentra regresa los valores
##          result=1 y id 0 para Admin
##
def accesosistema(user, password):
    result = 0
    idusuario = 0
    idnombre = None
    result, idusuario, idnombre = seguridadadmin(user, password)

    if result == 0:
        result, idusuario, idnombre = seguridadpaciente(user, password)

    print("accesosistema(): result= ", result, ",  idusuario=", idusuario, ",  usuaruio:", idnombre)
    return result, idusuario, idnombre


def seguridadadmin(user, password):
    # valores: 0. fallo, 1. correcto
    result = 0
    idusuario = 0
    nombre = "admin"
    if user == 'admin' and password == '1234':
        result = 1

    return result, idusuario, nombre

def seguridadpaciente (user,password):         
    # result: 0. fallo, 1. correcto
    result = 0
    # retorna el id que corresponde, si igual a cero no lo encontro
    idusuario = 0
    nombre = None

    if dg.gPacientes:    
        for obj in dg.gPacientes:    
            #print (obj.usuario," : ",user," == ",obj.password," : ",password)
            if str(obj.usuario) == str(user) and (obj.password == password):
                result = 2
                idusuario = obj.id
                nombre=obj.nombre
    print("=========================")            
    print ("seguridadpaciente()", "result", result,"idusuario",idusuario,"nombre",nombre)
    print("=========================")
    return result, idusuario, nombre