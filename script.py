#Created on 26 Dic. 2016
#@author: epena

import sys,argparse,zipfile,shutil,string,random,os

#Funciones

#Funcion para generar id para la carpeta temporal
def generator_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

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

#Verifico que el nombre del paquete sea el mismo nombre de la carpeta interna
if not z.namelist()[0][:-1] == os.path.splitext(package_param)[0]:
    print "Nombre del Zip:  %s:" % (filename)
    print "Nombre de la carpeta dentro del Zip:  %s: " % z.namelist()[0]
    print "El nombre del paquete no coincide con el nombre de la carpeta"
    sys.exit(1)




#zf = zipfile.ZipFile(package_param, 'r')
#zf.extractall(workDir) #Extraigo el contenido del zip en /tmp/e/
#zf.close()

#packageName = os.path.splitext(package_param)[0]
#a = workDir + '/' + packageName
#descompressedPackage = os.path.isdir(a)

#print workDir
#print descompressedPackage

#shutil.rmtree(workDir) #Borro carpeta temporal