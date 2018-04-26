import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import scipy.spatial.distance as ssd
import scipy.stats as ss

y, y0, pvalues= [], [], []

f=open("songs.txt", "r")
for linian in f:
    linia=linian.strip().split(",")
    for i in linia:
        y0.append(int(i))
    y.append(list(y0))
    y0=[]

y1, y2 = np.array(y[0]), np.array(y[1])

if len(y1)>len(y2):
    y1, y2= y2, y1

i=0
minim=len(y1)
ym=y2[0:minim]

while minim+i<len(y2):
    x1 = np.linspace(1, len(y1), len(y1))
    xm = x1
    # Interpolating now, using linear, but you can do better based on your data
    f = interp1d(x1, y1)
    fm = interp1d(xm ,ym)

    points = 15

    xnew1 = np.linspace ( min(x1), max(x1), num = points)
    xnewm = np.linspace ( min(xm), max(xm), num = points)

    ynew1 = f(xnew1)
    ynewm = fm(xnewm)
    #plt.plot(x1, y1, 'r', xm, ym, 'g', xnew1, ynew1, 'r--', xnewm, ynewm, 'g--')
    #plt.show()

    # Now compute correlations
    a=ssd.correlation(ynew1, ynewm) # Computes a distance measure based on correlation between the two vectors
    b=np.correlate(ynew1, ynewm, mode='valid') # Does a cross-correlation of same sized arrays and gives back correlation
    c=np.corrcoef(ynew1, ynewm) # Gives back the correlation matrix for the two arrays
    d=ss.spearmanr(ynew1, ynewm) # Gives the spearman correlation for the two arrays
    pvalues.append(d[1])
    i+=1
    ym=y2[i:minim+i]
    
#print(pvalues)
print(min(pvalues))
