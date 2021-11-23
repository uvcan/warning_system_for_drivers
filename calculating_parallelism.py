import numpy as np
def parallelism_calculation(lst1,lst2):
    n=len(lst1)
    x=np.array(lst1)
    y=np.array(lst2)
    xy = np.multiply(x,y)
    x2 = np.power(x,2)
    Sxy = np.sum(xy)
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sx2 = np.sum(x2)
    a = (Sxy - (Sx*Sy/n)) / (Sx2-(Sx*Sx/n))
    return a