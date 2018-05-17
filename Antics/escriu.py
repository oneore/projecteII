from direct_red import *

f=open("one_kiss.txt", 'a')
for i in freqs_t:
    f.write(str(i))
    if i!=freqs_t[-1]:
        f.write("\n")
f.close()
