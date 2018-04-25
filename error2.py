lista_canciones = ['Amelie.txt','chopin_nocturne92.txt'] #nuestra lista de canciones
f1 = open('record.txt','r')
record = f1.read().split('\n')[:-1]
adivinanza = ''

def er(record, cancion):
    if len(record) < len(cancion):
        lon = len(record)
    else:
        lon = len(cancion)

    error = 0
    for i in range (lon):
        error += (abs(float(record[i])-float(cancion[i])))**0.5
    return error/lon

for c in lista_canciones:
    f2 = open(c,'r')
    cancion = f2.read().split('\n')[:-1]
    errorMax = 1000000
    for i in range (0,150):
        error = er(record,cancion)
        #print(error)
        if errorMax > error:
            errorMax = error
            adivinanza = c[:-4]
        record = record[2:]

print(errorMax)
print(adivinanza)
