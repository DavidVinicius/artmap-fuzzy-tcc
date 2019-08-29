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

def groupCategories(IC, W, alpha = 0.0001):
    categories  = []
    for i in range(0, len(IC)):
        a       = np.sum(AND(IC[i], W[i]))
        temp    = round(a / (alpha + np.sum(W[i])), 5)
        categories.append(temp)
    return categories

def hadRessonance(IC, W, rho):
    x   = AND(IC, W)
    return ((sum(x) / sum(IC)) >= rho)

def learn(IC, W, beta):
    temp1   = beta * AND(IC, W)
    temp2   = (1 - beta) * IC
    return temp1 + temp2

