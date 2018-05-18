from direct_red0 import *

f=open("txt/No_Tears_Left_To_Cry_1_-_Ariana_Grande.txt", 'w')
for i in freqs_t:
    f.write("%s" % i[1])
    if i!=freqs_t[-1]:
        f.write("\n")

f.close()
