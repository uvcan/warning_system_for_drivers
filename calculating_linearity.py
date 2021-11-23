import numpy as np

def linearity_calculation(lst1,lst2):
    n=len(lst1)
    x = np.array(lst1)
    y = np.array(lst2)
    xy = np.multiply(x,y)
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sxy = np.sum(xy)
    x2 = np.power(x,2)
    y2 = np.power(y,2)
    Sx2 = np.sum(x2)
    Sy2 = np.sum(y2)
    #print(Sx)
    #print(Sy)
    #print(Sx2)
    #print(Sy2)
    #print(Sxy)

    R2 = (Sxy - Sx * (Sy/n))*(Sxy - Sx * (Sy/n))/((Sx2-(Sx*Sx)/n)*((Sy2)-(Sy*Sy)/n))
    print("                       R squared = ",R2)
    return R2

