from direct_red0 import *

f=open("havana.txt", 'w')
for i in freqs_t:
    f.write("%s" % i)
    if i!=freqs_t[-1]:
        f.write("\n")

f.close()
