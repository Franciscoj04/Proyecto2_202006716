import defglobal as dg
import json
from json import JSONEncoder

class usuario():
    
    #Constructor
    def __init__(self, idpaciente,nombre , sexo, usuario, apellido, password):

        if idpaciente > 0:
            self.id=idpaciente
        else:
            self.id = next(dg.nopaciente)
            
        self.nombre = nombre
        self.sexo = sexo
        self.usuario = usuario
        self.apellido = apellido
        self.password = password

    #Getters
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
                 
    def getSexo(self):
        return self.sexo         

    def getUsuario(self):
        return self.usuario
    
    def getApellido(self):
        return self.apellido 

    def getPassword(self):
        return self.password
          
   
    #Setters
    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre

    def setSexo(self, sexo):
        self.sexo = sexo

    def setUsuario(self, usuario):
        self.usuario = usuario   

    def setApellido(self, apellido):
        self.apellido = apellido 

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
                return [obj.id,obj.nombre,obj.sexo, obj.usuario, obj.apellido, obj.password]
            i=i+1    
        return []

class PacienteEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__        
