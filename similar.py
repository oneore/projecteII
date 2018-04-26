from spear import *

pvalors={}

for song in ["txt/shape_of_you.txt", "txt/new_rules.txt"]:
    f=open(song, 'r')
    full=f.read().strip().split(',')
    pvalors[minpvalue(full)]=song

mini=min(pvalors.keys())
print(pvalors)
print(pvalors[mini])
