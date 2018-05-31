from direct_red0 import *

f=open("txt/Back_To_Black_-_Amy_Winehouse.txt", 'w')
for i in freqs_t:
    f.write("%s" % i[1])
    if i!=freqs_t[-1]:
        f.write("\n")
f.close()
