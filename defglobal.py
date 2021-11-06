import itertools
import os
#############################################
# definicion lista globales
#############################################
global gPacientes
gPacientes = []

global gMedicos
gMedicos = []

global gEnfermeras
gEnfermeras = []

global gMedicamentos
gMedicamentos = []

global gCitas
gCitas = []

global gCompras
gCompras = []

global gFacturas
gFacturas = []
#############################################
# Variables Globales
#############################################
global delimitador
delimitador = ","

### Define idusuario y idnombre para capturar el id del usuario logueado.
global idusuario
idusuario=0

global idnombre
idnombre = None

#### define autoincremental
global nopaciente
nopaciente = itertools.count(1,1)

global nocita
nocita = itertools.count(1,1)

global nocompra
nocompra = itertools.count(1,1)

global noproducto
noproducto = itertools.count(1,1)



global MYDIR
#MYDIR = os.path.dirname(__file__)
MYDIR = "/tmp/"
