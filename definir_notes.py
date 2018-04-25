from direct import *
import numpy as np

global l
llista = l
#print(llista)
freq_tract=[]
nota=[]
cont=0

for i in range(1, len(llista)-1):
    if (-10+llista[i+1]<=llista[i]<=10+llista[i+1]):
        nota.append(llista[i+1])
        cont+=1
    else:
        nota=[]
        cont=0
    if cont>=3:
        sum=0
        cont1=0
        for j in nota:
            sum+=j
            cont1+=1
        mitj=sum/cont1
        freq_tract.append(mitj)
        mitj=0
        cont=0
        nota=[]

#print(llista)
#print(freq_tract)

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

llista_notes=[]
llista_freqs=[]
for f in freq_tract:
    A=np.fromiter(dicc.keys(), dtype=float)
    idx=(np.abs(A-f)).argmin()
    a=format(A[idx], '.2f')
    llista_freqs.append(a)
    llista_notes.append(dicc[a])

#print(llista_notes)

llista_def=[]
llista_freqs_def=[]
for i in llista_notes:
    if i not in llista_def:
        llista_def.append(i)
for i in llista_freqs:
    if i not in llista_freqs_def:
        llista_freqs_def.append(i)

print(llista_def, llista_freqs_def)
#print(llista_freqs_def)
