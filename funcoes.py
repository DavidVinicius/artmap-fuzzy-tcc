import numpy as np


def normalize(arr, valueMax = 0):
    if valueMax == 0:
        valueMax = arr.max()

    I  = np.divide(arr, valueMax)
    return I

def complement(I):
    IC = np.subtract(1, I)
    A  = []

    for i in range(0, len(I)):
        #print(np.concatenate((I[i], IC[i])))
        #I[i].extend(list(IC))
        A.append( np.concatenate((I[i], IC[i])) )
    
    return np.array(A)

def AND(arr1, arr2):
    I = []
    for i in range(0, len(arr1)):
        I.append(min(arr1[i], arr2[i]))
    return I

