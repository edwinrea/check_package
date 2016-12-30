#Created on 26 Dic. 2016
#@author: epena

import sys,argparse,zipfile,shutil,string,random,os,re,datetime,fnmatch

exeption_folder = ['master']
allowed_files = ['central.sql','caja.sql','server.sql','caja-propiedades.txt','server-propiedades.txt']
configurator_files = ['VersionGEOPosServer.xml','VersionGEOPosCaja.xml']

#Funciones

#Funcion para ordenar naturalmente una lista
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def is_exception_folder(folder):
    return folder in exeption_folder

def is_allowed_file(file):
    return file in allowed_files

def is_allowed_configurator(file):
    return file in configurator_files

def delete_content(pfile):
    pfile.seek(0)
    pfile.truncate()

def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
               result.append(os.path.join(root, name))
    return result

execution_folder = os.path.abspath(os.path.dirname(__file__))

#Creacion de la carpeta temporal
folder_name = unicode(datetime.datetime.now())
work_dir = '/tmp/' + folder_name

print work_dir


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

#Renombro el zip
package_param_old = package_param + '_old'

os.rename(package_param,package_param_old)

module_name = z.namelist()[0]

#Verifico que el nombre del paquete sea el mismo nombre de la carpeta interna
if not z.namelist()[0][:-1] == os.path.splitext(package_param)[0]:
    print "Nombre del Zip:  %s:" % package_param
    print "Nombre de la carpeta dentro del Zip:  %s: " % module_name
    print "El nombre del paquete no coincide con el nombre de la carpeta"
    #Borro carpeta temporal
    shutil.rmtree(work_dir)
    sys.exit(1)

#Asignacion de la ruta donde se encuentra el modulo descomprimido

module_path = work_dir+"/"+module_name

docs = module_path + "docs/"

docs_folder=os.listdir(docs)

#Me cambio al directorio Docs
os.chdir(docs)



the_file = open(docs + '/versiones.txt', 'w+')
delete_content(the_file)

versiones = []
configuraciones = []

for dir in docs_folder:

    if not is_exception_folder(dir):
        if os.path.isdir(dir):
            versiones.append(dir)
            for file in os.listdir(dir):
                if not is_allowed_file(file):
                    print "WARNING: Archivo no permitido "+ dir +" " + file
        elif is_allowed_configurator(dir):
            configuraciones.append(dir)

#Armo el versiones.txt ordenadamente
for item in natural_sort(versiones):
    print >> the_file,item

if not configuraciones:
    print "NO SE ENCONTRO ARCHIVO DE CONFIGURATOR"
    exit(1)

#Cierro el archivo versiones
the_file.close()

os.chdir(work_dir)

make_zipfile(package_param,module_name)

shutil.copy2(package_param,execution_folder)

#Borro carpeta temporal
shutil.rmtree(work_dir)