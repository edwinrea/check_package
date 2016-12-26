#Created on 26 Dic. 2016
#@author: epena

import sys,argparse,zipfile,shutil,string,random,os

#Funciones

def generator_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

folderName = generator_id()
workDir = '/tmp/' + folderName

parser = argparse.ArgumentParser(description="Validador de paquetes")
parser.add_argument('-p', '--package', nargs='?', help='Paquete a validar', required=True)
args = parser.parse_args()

package_param = args.package #Obtengo el nombre del parametro

zf = zipfile.ZipFile(package_param, 'r')
zf.extractall(workDir) #Extraigo el contenido del zip en /tmp/e/
zf.close()

packageName = os.path.splitext(package_param)[0]
a = workDir + '/' + packageName
descompressedPackage = os.path.isdir(a)

print workDir
print packageName

shutil.rmtree(workDir) #Borro carpeta temporal