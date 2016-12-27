#Created on 26 Dic. 2016
#@author: epena

import sys,argparse,zipfile,shutil,string,random,os,re

#Funciones

#Funcion para generar id para la carpeta temporal
def generator_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Funcion para ordenar naturalmente una lista
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


#Lista con pablabras a eliminar
black_list = ['master']

print str(black_list)

#Creacion de la carpeta temporal
folderName = generator_id()
workDir = '/tmp/' + folderName

#Se parsea los argumentos
parser = argparse.ArgumentParser(description="Validador de paquetes")
parser.add_argument('-p', '--package', nargs='?', help='Paquete a validar', required=True)
args = parser.parse_args()

#Obtengo el nombre del paquete
package_param = args.package

#Verifico el nombre de la carpeta del Zip
for filename in sys.argv[2:]:
    z = zipfile.ZipFile(file(filename))

#Extraigo el contenido del zip en carpeta temporal
zf = zipfile.ZipFile(package_param, 'r')
zf.extractall(workDir)
zf.close()

#Verifico que el nombre del paquete sea el mismo nombre de la carpeta interna
if not z.namelist()[0][:-1] == os.path.splitext(package_param)[0]:
    print "Nombre del Zip:  %s:" % (filename)
    print "Nombre de la carpeta dentro del Zip:  %s: " % z.namelist()[0]
    print "El nombre del paquete no coincide con el nombre de la carpeta"
    #Borro carpeta temporal
    shutil.rmtree(workDir)
    sys.exit(1)

#Asignacion de la ruta donde se encuentra el modulo descomprimido
module_path = workDir+"/"+z.namelist()[0]+"docs/"

#for a in os.listdir(module_path):
#   print a

#for root, dirnames, filenames in os.walk(module_path):
#    print root

os.chdir(module_path)
print os.getcwd()


dir_list = os.walk(module_path).next()[1]
#dir_list = [f for f in dir_list if "master" not in f]
dir_list = remove_values_from_list(dir_list,black_list)
#print  masterless_versiones

#if any("master" in s for s in dir_list):
#    print "edwin"

thefile = open('versiones.txt', 'w')

for item in natural_sort(dir_list):
    print>>thefile, item


#shutil.rmtree(workDir) #Borro carpeta temporal