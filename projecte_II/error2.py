lista_canciones = ['Amelie_Le_moulin.txt','chopin_nocturne92.txt','mine.txt','Intouchables.txt','Deja vu, Shakira.txt','Shape of you.txt'] #nuestra lista de canciones
adivinanza = ''

def er(record, cancion):
    if len(record) < len(cancion):
        lon = len(record)
    else:
        lon = len(cancion)

    error = 0
    suma = 0
    for i in range (lon):
        if record[i] != '0':
            error += (abs(float(record[i])-float(cancion[i])))**0.5
            suma += 1
    return error/suma

errorMax = 1000
for c in lista_canciones:
    f2 = open(c,'r')
    cancion = f2.read().split('\n')[:-1]
    f1 = open('prueba.txt','r')
    record = f1.read().split('\n')[:-1]
    for i in range (0,100):
        error = er(record,cancion)
        if errorMax > error:
            errorMax = error
            adivinanza = c[:-4]
            print (adivinanza)
        record = record[2:]

print(errorMax)
print(adivinanza)

#'Amelie_Le_moulin.txt','chopin_nocturne92.txt','mine.txt'
