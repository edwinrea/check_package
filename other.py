import zipfile,sys

for filename in sys.argv[1:]:
        z = zipfile.ZipFile(file(filename))
        print "%s:" % (filename)
        print z.namelist()[0]
        for f in z.namelist():
                print "\t%s" % (f)
        print ""



exception_list={"master","peteco"}


#def is_excepcion(carpeta):


#recorro para cada carpeta de la lista de carpetas dentro de docs.

        #si carpeta not in expeption_list:
                #escribo en versiones.txt
                #check_script_files(carpeta)
        #sino no hago nada


