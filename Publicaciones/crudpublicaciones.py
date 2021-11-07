import defglobal as dg
import Publicaciones.publicacion as classm

def setUpdateData(id, nombre, sexo, usuario, apellido, password):
        #dg.gPacientes = [obj for obj in dg.gPacientes if str(obj.id) != str(id)]
        for obj in dg.gMedicos:    
            print (obj.id," ==== ",id)
            if str(obj.id) == str(id):
                dg.gMedicos.remove(obj)
        newobj = classm.publicacion(id, nombre, sexo, usuario, apellido, password )
        dg.gMedicos.append(newobj)

def deleteData(id):
    #dg.gPacientes = [obj for obj in dg.gPacientes if obj.id == id]  
    for obj in dg.gMedicos:    
        print (obj.id," ==== ",id)
        if str(obj.id) == str(id):
            dg.gMedicos.remove(obj)



def getdoctor(idusuario):
    nombre = None
    sexo = None
    usuario = None
    apellido = None
    password = None
    for obj in dg.gMedicos:    
        
        if str(obj.id) == str(idusuario):
            nombre = obj.nombre
            sexo = obj.sexo
            usuario = obj.usuario
            apellido = obj.apellido
            password = obj.password
            
    print ("getdoctor(): ",nombre," ==== ",apellido)
    return idusuario,nombre, sexo, usuario,apellido, password

def getnombredoctor(iddoctor):
    nombres = None
    for obj in dg.gMedicos:    
        
        if str(obj.id) == str(iddoctor):
            nombres = obj.nombre + " " +obj.apellido
    print("Nombres del Doctor :",nombres)
    return nombres

def listToHTML():
        t = '<table  border="1" class="dataframe table-condensed" id="tableMedicos" style="width=60%; font-size:13px; line-height:8px;" >'
        header =['Id','Nombres','Sexo','Usuario', 'Appellido','Password',] 
        t = t + '<tr> <thead>'
        for h in header:
               t = t + '<th>' +h+' </th>'
        t = t + '</thead> </tr>'
        r = '<tbody id="tableBody">'
        if dg.gMedicos:
            for obj in dg.gMedicos:
                r = r + '<tr>'
                r = r + '<td name="idMedico" id="idMedico" stye="font-size: 10px">'+ str(obj.id) + '</td>'
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
        return t    

def listToPrint():
        print("==== Listado de publicaciones ==== ")
        for obj in dg.gMedicos:
            print( obj.id,obj.nombre, obj.sexo,obj.usuario,obj.apellido,obj.password,  sep ='\t' )

   

def ListtoJSON():
        obj = dg.gMedicos
        jsonstr = json.dumps(obj, indent=4, cls=MedicoEncoder)
        return jsonstr         


