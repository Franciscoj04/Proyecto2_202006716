import defglobal as dg
import json
from json import JSONEncoder

class usuario():
    
    #Constructor
    def __init__(self, idpaciente,nombre , apellido, fecha, sexo, usuario, password):

        if idpaciente > 0:
            self.id=idpaciente
        else:
            self.id = next(dg.nopaciente)
            
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.sexo = sexo
        self.usuario = usuario
        self.password = password

    #Getters
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido        

    def getfecha(self):
        return self.fecha          

    def getSexo(self):
        return self.sexo         

    def getUsuario(self):
        return self.usuario

    def getPassword(self):
        return self.password
          
   
    #Setters
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setFecha(self, fecha):
        self.fecha = fecha

    def setSexo(self, sexo):
        self.sexo = sexo

    def setUsuario(self, usuario):
        self.usuario = usuario    

    def setPassword(self, password):
        self.password = password  

    # Other Methods

    def toJSON(self):
        return json.dumps(self, cls=PacienteEncoder, sort_keys=True, indent=4)  

     

    def getData(self, id):
        obj = dg.gPacientes
        i=0
        for obj in dg.gPacientes:
            if obj.id == id:
                return [obj.id,obj.nombre, obj.apellido, obj.fecha,obj.sexo, obj.usuario, obj.password]
            i=i+1    
        return []

class PacienteEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__        
