from direct_red import *
import numpy as np
from compara import *

llista=freqs
buit=np.array([])
freq_tract, nota, cont = buit, buit, 0

for i in range(1, len(freqs)-1):
    if (-10+freqs[i+1]<=freqs[i]<=10+freqs[i+1]):
        nota=np.insert(nota, 0, llista[i+1])
        cont+=1
    else:
        nota, cont = buit, 0
    if cont>=3:
        freq_tract=np.insert(freq_tract, 0, np.mean(nota))
        nota=buit
"""
Notes=del_reps(nota_propera(freq_tract, compara())[0])
Freqs_notes=del_reps(nota_propera(freq_tract, compara())[1])
print(Notes)
print(Freqs_notes)
"""
