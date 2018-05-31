from direct_red0 import *

f=open("txt/Paranoid_-_Black_Sabbath.txt", 'w')
for i in freqs_t:
    f.write("%s" % i[1])
    if i!=freqs_t[-1]:
        f.write("\n")
f.close()
