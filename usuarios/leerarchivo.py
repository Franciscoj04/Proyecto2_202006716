import os
import csv
import json
import usuarios.usuario as classP
import usuarios.crudusuario as crudP
import defglobal as dg

# leer archivo CSV y pasarlo a Json

def readCSVofPacientes(obj,filename, delimter):
    try: 
        with open(filename, "r") as f:
            line = f.readline().strip().split(delimter)
            line = f.readline().strip().split(delimter)
            i = 1
           
            while line != ['']:
                existe = False;
                line = line[0].split(" ") + line[1:]
                #print ("Pacientes",line)
                o=obj.Paciente(-1,line[0], line[1], line[2], line[3], line[4],line[5],line[6])

                ## Valida primero que no exista
                for r in dg.gPacientes:    
                    if r.usuario.lower() == o.usuario.lower(): 
                        existe = True;
                
                if not existe:
                    dg.gPacientes.append(o)

                line = f.readline().strip().split(delimter)
                i = i+1
            print ("Total pacientes cargados: ",i)
        return o    
    except IOError:
        pass
    
def getFilePaciente(csvFilePath):
    obj = classP
    #dg.gPacientes.clear()
    r=readCSVofPacientes(obj,csvFilePath,dg.delimitador)
    html = crudP.listToHTML()

    return html
     



