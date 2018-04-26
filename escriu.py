from direct_red import *

f=open("songs.txt", 'a')
for i in freqs_t:
    f.write(str(i))
    f.write(",")
f.write("\n")
f.close()
