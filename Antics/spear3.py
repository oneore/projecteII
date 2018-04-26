import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import scipy.spatial.distance as ssd
import scipy.stats as ss

x = np.linspace(0, 20, num=70)
x2 = np.linspace(1, 11, num=13)

y = 2*np.sin(x) + 4 + np.random.random(len(x))
y2 = 2* np.cos(x2) + 5 + np.random.random(len(x2))

# Interpolating now, using linear, but you can do better based on your data
f = interp1d(x, y)
f2 = interp1d(x2,y2)

points = 15

xnew = np.linspace ( min(x), max(x), num = points)
xnew2 = np.linspace ( min(x2), max(x2), num = points)

ynew = f(xnew)
ynew2 = f2(xnew2)
plt.plot(x,y, 'r', x2, y2, 'g', xnew, ynew, 'r--', xnew2, ynew2, 'g--')
plt.show()

# Now compute correlations
print (ssd.correlation(ynew, ynew2)) # Computes a distance measure based on correlation between the two vectors
print (np.correlate(ynew, ynew2, mode='valid')) # Does a cross-correlation of same sized arrays and gives back correlation
print (np.corrcoef(ynew, ynew2)) # Gives back the correlation matrix for the two arrays

print (ss.spearmanr(ynew, ynew2)) # Gives the spearman correlation for the two arrays
