f=open('notes.txt', 'r')
llista=[]
dicc={}
for linian in f:
    linia=linian.strip().split()
    llista.append(linia)
del[llista[0]]
for i in llista:
    dicc[i[1]]=i[0]

#print(dicc)
#print(list(dicc.keys())[0])

def def_notes(l):
    compas = []
    cont = 0
    nota_anterior = l[0]
    for i in range (len(l)-1):
        nueva_nota = l[i+1]
        if nueva_nota+8 > nota_anterior or nueva_nota-8 < nota_anterior:
            cont += 1
        else:
            if cont < 4:     #8 notas por 1 tiempo
                nota = 'c16' silencio
            elif cont < 4:
                
            cont = 0
