#Created on 26 Dic. 2016
#@author: epena

import sys,argparse,zipfile,shutil,string,random,os,re

exeption_folder = ['master']
allowed_files = ['central.sql','caja.sql','server.sql','caja-propiedades.txt','server-propiedades.txt']

#Funciones

#Funcion para generar id para la carpeta temporal
def generator_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#Funcion para ordenar naturalmente una lista
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def is_exception_folder(folder):
    return folder in exeption_folder

def is_allowed_file(file):
    return file in allowed_files

def delete_content(pfile):
    pfile.seek(0)
    pfile.truncate()


#Lista con pablabras a eliminar
black_list = ['master','VersionGEOPosServer.xml']

#Creacion de la carpeta temporal
folder_name = generator_id()
work_dir = '/tmp/' + folder_name

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
zf.extractall(work_dir)
zf.close()

#Verifico que el nombre del paquete sea el mismo nombre de la carpeta interna
if not z.namelist()[0][:-1] == os.path.splitext(package_param)[0]:
    print "Nombre del Zip:  %s:" % (filename)
    print "Nombre de la carpeta dentro del Zip:  %s: " % z.namelist()[0]
    print "El nombre del paquete no coincide con el nombre de la carpeta"
    #Borro carpeta temporal
    shutil.rmtree(work_dir)
    sys.exit(1)

#Asignacion de la ruta donde se encuentra el modulo descomprimido
module_path = work_dir+"/"+z.namelist()[0]
docs = module_path + "docs/"

docs_folder=os.listdir(docs)

os.chdir(docs)

the_file = open('versiones.txt', 'w+')
delete_content(the_file)

versiones = []
for dir in docs_folder:
    if not is_exception_folder(dir):
        if os.path.isdir(dir):
            versiones.append(dir)
        else:
            continue
        print dir
        for file in os.listdir(dir):
            if not is_allowed_file(file):
                if file.endswith('.sql'):
                    if not is_allowed_file(file):
                        print "ERROR" + file
                elif file.endswith('.txt'):
                    if not is_allowed_file(file):
                        print "***********************ERROR " + file
                continue
            else:
                print file

#Armo el versiones.txt ordenadamente
for item in natural_sort(versiones):
    print >> the_file,item

the_file.close()

#Borro carpeta temporal
shutil.rmtree(work_dir)