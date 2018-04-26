import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import scipy.spatial.distance as ssd
import scipy.stats as ss

y, y0= [], []

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

min=len(y1)


x1, x2 = np.linspace(1, len(y1), len(y1)), np.linspace(1, len(y2), len(y2))

# Interpolating now, using linear, but you can do better based on your data
f = interp1d(x1, y1)
f2 = interp1d(x2 ,y2)

points = 15

xnew1 = np.linspace ( min(x1), max(x1), num = points)
xnew2 = np.linspace ( min(x2), max(x2), num = points)

ynew1 = f(xnew1)
ynew2 = f2(xnew2)
plt.plot(x1, y1, 'r', x2, y2, 'g', xnew1, ynew1, 'r--', xnew2, ynew2, 'g--')
plt.show()

# Now compute correlations
a=ssd.correlation(ynew1, ynew2)) # Computes a distance measure based on correlation between the two vectors
b=np.correlate(ynew1, ynew2, mode='valid')) # Does a cross-correlation of same sized arrays and gives back correlation
c=np.corrcoef(ynew1, ynew2)) # Gives back the correlation matrix for the two arrays
d=ss.spearmanr(ynew1, ynew2)) # Gives the spearman correlation for the two arrays
