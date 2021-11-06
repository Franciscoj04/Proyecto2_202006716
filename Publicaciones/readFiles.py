import os
import csv
import json
import Publicaciones.publicacion as classM
import Publicaciones.crudpublicaciones as crudM
import defglobal as dg

# leer archivo CSV y pasarlo a Json

def readCSVofMedicos(obj,filename, delimter):
    try:
        with open(filename, "r") as f:
            line = f.readline().strip().split(delimter)
            line = f.readline().strip().split(delimter)
            i = 1
            while line != ['']:
                line = line[0].split(" ") + line[1:]
                o=obj.Medico(i,line[0], line[1], line[2], line[3], line[4],line[5],line[6],line[7])
                dg.gMedicos.append(o)
                line = f.readline().strip().split(delimter)
                i = i+1
        return o    
    except IOError:
        pass

def getFileMedico(csvFilePath):
    obj = classM
    dg.gMedicos.clear()
    r=readCSVofMedicos(obj,csvFilePath,dg.delimitador)
    html = crudM.listToHTML()

    return html
     
