from direct_red0 import *

f=open("txt/Let_It_Loose_-_Rolling_Stones.txt", 'w')
for i in freqs_t:
    f.write("%s" % i[1])
    if i!=freqs_t[-1]:
        f.write("\n")
f.close()
