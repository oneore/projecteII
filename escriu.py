from direct_red import *

f=open("songs.txt", 'a')
for i in freqs_t:
    f.write(str(i))
    if i!=freqs_t[-1]:
        f.write(",")
f.close()
