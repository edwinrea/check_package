import sys,argparse,zipfile

parser = argparse.ArgumentParser(description="Validador de paquetes")
parser.add_argument('-p', '--package', nargs='?', help='Paquete a validar', required=True)
args = parser.parse_args()

package_param = args.package

print package_param

zf = zipfile.ZipFile(package_param, 'r')

print zf.namelist()