import numpy as np

def dist(A, B):
  # r = np.sqrt(np.sum((A-B)**2))
  r = np.abs(np.sum((A-B)))
  return r

def class_of_each_point(X, centers):
  m = len(X)
  k = len(centers)

  distances = np.zeros((m, k))
  for i in range(m):
    for j in range(k):
       distances[i, j] = dist(centers[j], X[i])

  return np.argmin(distances, axis=1)


def kmeans(k, X):
    m = X.shape[0]
    n = X.shape[1]

    curr_iteration = prev_iteration = np.zeros(m)

    centers = np.random.random((k, n))
    
    centers = centers * (np.max(X, axis=0) - np.min(X, axis=0)) + np.min(X, axis=0)
    
    curr_iteration = class_of_each_point(X, centers)

    while np.any(prev_iteration != curr_iteration):
        prev_iteration = curr_iteration
        for i in range(k):
          sub_X = X[curr_iteration == i,:]
          if len(sub_X) > 0:
            centers[i,:] = np.mean(sub_X, axis=0)
        curr_iteration = class_of_each_point(X, centers)
    return centers