import sys,argparse,zipfile,uuid,shutil

folderName = str(uuid.uuid4())
workDir = '/tmp/' + folderName

print (workDir)


parser = argparse.ArgumentParser(description="Validador de paquetes")
parser.add_argument('-p', '--package', nargs='?', help='Paquete a validar', required=True)
args = parser.parse_args()

package_param = args.package #Obtengo el nombre del parametro

zf = zipfile.ZipFile(package_param, 'r')
zf.extractall(workDir) #Extraigo el contenido del zip en /tmp/e/
zf.close()

shutil.rmtree(workDir) #Borro carpeta temporall