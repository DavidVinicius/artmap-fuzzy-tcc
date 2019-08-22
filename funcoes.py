import numpy as np


def normalize(arr, valueMax = 0):
    if valueMax == 0:
        valueMax = arr.max()

    I  = np.divide(arr, valueMax)
    return I

def complement(I):
    IC = np.subtract(1, I)
    A  = []

    for i in range(0, 2):
        #print(np.concatenate((I[i], IC[i])))
        A.append( np.concatenate((I[i], IC[i])) )
    
    return np.array(A)
