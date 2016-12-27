import zipfile,sys

for filename in sys.argv[1:]:
        z = zipfile.ZipFile(file(filename))
        print "%s:" % (filename)
        print z.namelist()[0]
        for f in z.namelist():
                print "\t%s" % (f)
        print ""