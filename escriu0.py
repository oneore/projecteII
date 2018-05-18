from direct_red0 import *

f=open("txt/no_tears_left_to_cry.txt", 'w')
for i in freqs_t:
    f.write("%s" % i[1])
    if i!=freqs_t[-1]:
        f.write("\n")

f.close()
