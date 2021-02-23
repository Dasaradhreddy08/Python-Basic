try:
    fl=open("filen.txt","r")
except IOError:
    print("IOError : file not found erro ")
else:
    print("file opened successfully ")
    fl.close()