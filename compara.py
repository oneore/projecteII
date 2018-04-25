import numpy as np

def compara():
    f=open('notes.txt', 'r')
    llista=[]
    dicc={}
    for linian in f:
        linia=linian.strip().split()
        llista.append(linia)
    del[llista[0]]
    for i in llista:
        dicc[i[1]]=i[0]
    return dicc

def nota_propera(freq_tract, dicc):
    llista_notes=[]
    llista_freqs=[]
    for f in freq_tract:
        A=np.fromiter(dicc.keys(), dtype=float)
        idx=(np.abs(A-f)).argmin()
        a=format(A[idx], '.2f')
        llista_freqs.append(a)
        llista_notes.append(dicc[a])
    return llista_notes, llista_freqs

def del_reps(llista):
    llista_def=[]
    for i in llista:
        if i not in llista_def:
            llista_def.append(i)
    llista_def=llista_def[::-1]
    return llista_def
