import numpy as np
import math

def k_nearest(X, k, obj, r):
    sub_X = X[:, 0:-1]
    mean = np.mean(sub_X, axis=0)
    std = np.std(sub_X, axis=0)

    normal_X = (sub_X - mean) / std

    normal_obj = (obj - mean) / std

    if(r == 1):
        d = [Evklid(normal_obj, i) for i in normal_X]
    if(r == 2):
        d = [Evklid(normal_obj, i) for i in normal_X]
    if(r == 3):
        d = [Hemming(normal_obj, i) for i in normal_X]

    nb = np.argsort(d)

    nearest_classes = X[nb[0:k], 2]
    unique, counts = np.unique(nearest_classes, return_counts=True)
    object_class = unique[np.argmax(counts)]

    return object_class
    
def Evklid(p1, p2):
    return math.sqrt(sum((p1 - p2)**2))

def Hemming(p1, p2):
    return sum(abs(p1-p2))

def Minkowski(p1, p2):
    p = 2
    r = 2
    return sum(abs(p1-p2)^p)^(1/r)