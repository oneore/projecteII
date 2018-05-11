l_canciones = ['Amelie.txt']
err=0
error_max = 0
adivinanza=''
fr=0

def long(e,n):
    if len(open(e).readlines()) > len(open('prueba.txt').readlines())-n:
        return len(open('prueba.txt').readlines())-n
    else:
        return len(open(e).readlines())

for e in l_canciones:
    cancion = open(e, 'r')
    for n in range(200):
        f = open('prueba.txt', 'r')
        #for m in range(n):
         #   f.readline()
        longitud = long(e,n)
        for z in range(8):
            #print(str(z))
            fr = f.readline()
            cr = cancion.readline()
            #print(str(float(cr[:-1])))
            #print(str(int(fr[:-1])))
            print(float(cr[:-1])-float(fr[:-1]))
            err += abs(float(cr[:-1])-float(fr[:-1]))
        if error_max < err:
            error_max = err
            adivinanza = e
        err=0
        f.close()
    cancion.close()
    print('hola')
print(error_max)
print(adivinanza)
