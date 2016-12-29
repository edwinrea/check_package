#exception_list={"master","peteco"}


#def is_excepcion(carpeta):


#recorro para cada carpeta de la lista de carpetas dentro de docs.

        #si carpeta not in expeption_list:
                #escribo en versiones.txt
                #check_script_files(carpeta)
        #sino no hago nada

exeptionFolder = ['folder2']
WhiteFiles = ['central.sql','server.sql','caja.sql']

rray=['local','central','server.sql','folder1']


def is_exception_folder(folder):
    return folder in exeptionFolder


mypath='/tmp/python/'

import os

for dirname,dirnames, filenames in os.walk(mypath):
    # print path to all subdirectories first.
         for subdirname in dirnames:
            if not is_exception_folder(subdirname):
                print subdirname
                for file in os.walk(subdirname):
                        print file


    #for filename in filenames:
            #if '11' in filenames:
             #       filenames.remove('11')
    #                print(os.path.join(dirname, filename))

    # Advanced usage:
    # editing the 'dirnames' list will stop os.walk() from recursing into there.




