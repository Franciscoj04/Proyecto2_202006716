import defglobal as dg
import usuarios.usuario as classp

def insertPaciente(nombre, sexo, usuario, apellido, password):
    newobj = classp.usuario(-1, nombre, sexo, usuario, apellido, password)
    dg.gPacientes.append(newobj)

def setUpdateData(idpaciente, nombre, sexo, usuario, apellido, password):
        #dg.gPacientes = [obj for obj in dg.gPacientes if str(obj.id) != str(id)]
        for obj in dg.gPacientes:    
            print (obj.id," ==== ",idpaciente)
            if str(obj.id) == str(idpaciente):
                dg.gPacientes.remove(obj)
        newobj = classp.usuario(idpaciente, nombre, sexo, usuario, apellido, password)
        dg.gPacientes.append(newobj)

def deleteData(id):
    #dg.gPacientes = [obj for obj in dg.gPacientes if obj.id == id]  
    for obj in dg.gPacientes:    
        print (obj.id," ==== ",id)
        if str(obj.id) == str(id):
            dg.gPacientes.remove(obj)

def getpaciente(idusuario):
    nombre = None
    sexo = None
    usuario = None
    apellido = None
    password = None
    for obj in dg.gPacientes:    
        
        if str(obj.id) == str(idusuario):
            nombre = obj.nombre
            sexo = obj.sexo
            usuario = obj.usuario
            apellido = obj.apellido
            password = obj.password
            
    print ("getpaciente(): ",nombre," ==== ",apellido)
    return idusuario,nombre, sexo, usuario,apellido, password

### Si existe usuario retorna TRUE, sino FALSE
def getvalidusername(username):
    result = False
    for obj in dg.gPacientes:    
        if str(obj.usuario) == str(username):
            result = True
    return result            

def listToHTML():
        t = '<table  border="1" class="dataframe table-condensed" id="tablePacientes" style="width=60%; font-size:13px; line-height:8px;" >'
        header =['Id','Nombres', 'Sexo','Usuario','Correo','Password',] 
        t = t + '<tr> <thead>'
        for h in header:
               t = t + '<th>' +h+' </th>'
        t = t + '</thead> </tr>'
        r = '<tbody id="tableBody">'
        if dg.gPacientes:
            for obj in dg.gPacientes:
                r = r + '<tr>'
                r = r + '<td name="idPaciente" id="idPaciente" stye="font-size: 10px">'+ str(obj.id) + '</td>'
                r = r + '<td stye="font-size: 10px">'+ obj.nombre + '</td>'
                r = r + '<td>'+ obj.sexo + '</td>'
                r = r + '<td>'+ obj.usuario + '</td>'
                r = r + '<td>'+ obj.apellido + '</td>'
                r = r + '<td>'+ obj.password + '</td>'
                r = r + '<td><button type="button" id="editButton" class="btn btn-primary" onclick="editRow(event);">Visualize/Edit</button></td>'
                r = r + '<td><button type="button" id="deleteButton" class="btn btn-danger" onclick="deleteRow(event);">Delete</button></td>'
                r = r + '</tr>'
        t = t + r
        t = t + '</tbody>'
        t = t + '</table>'
        #print("tabla html",t)
        return t    

def listToPrint():
        print("==== Listado de usuarios ==== ")
        for obj in dg.gPacientes:
            print( obj.id,obj.nombre,obj.sexo,obj.usuario,obj.apellido,obj.password,  sep ='\t' )

   

def ListtoJSON():
        obj = dg.gPacientes
        jsonstr = json.dumps(obj, indent=4, cls=PacienteEncoder)
        return jsonstr         
