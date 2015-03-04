import math
import random
import re

'''
----------------------------------------------------------------
0. Common
----------------------------------------------------------------
'''

def nGram(d, N = 1):
    nGram = {}
    nGram.clear()
    key = ""
    prevWord1 = "<S>"
    prevWord2 = "<S>"
    
    data = ['<S>','<S>']
    data += d
    for word in data:
        if N == 1:
            key = word #unigram key
        elif N == 2:
            key = word + "|" + prevWord1 #bigram key
        elif N == 3:
            key = word + "|" + prevWord2 + " " + prevWord1 #trigram key
    
        if nGram.has_key(key): # calculate counts of n-gram
            nGram[key] = nGram[key] + 1
        else:
            nGram[key] = 1
        prevWord2 = prevWord1
        prevWord1 = word
    if N == 1:
        nGram['<S>'] = 1 #fix count of start key for unigram
    elif N == 2:
        nGram['<S>|<S>'] = 1 #fix count of start key for bigram
    return nGram;

def getKeys(strKey, N = 2):
    strKeys = []
    if N == 2:
        strKeys = strKey.split("|")
    elif N == 3:
        strKeys = re.split('[\|| ]', strKey)
        
    return strKeys

'''
----------------------------------------------------------------
1. Entropy of a Text
----------------------------------------------------------------
'''

def condEntropy(uniGram, biGram):
    H = 0
    total = sum(uniGram.values())
    
    for key in biGram:
    
        pJoined = biGram[key] / (1.0 * total) #joined probability
        pCond = biGram[key] / (1.0 * uniGram[getKeys(key)[1]]) #conditional probability
    
        H -= pJoined * math.log(pCond,2)
    
    return H

def replaceWords(d, p):
    random.seed(1)
    
    data = d
    words = list(set(data)) #make words from list unique
    sample = int(round(len(data) * (p / 100.0))) #how many replace based on probability
    
    while sample:
        sample = sample - 1
        i = random.randint(1, len(data)-1)
        j = random.randint(1, len(words)-1)
        data[i] = words[j]

    return data

def replaceChars(d, p):
    random.seed(1)
    
    data = d
    ch = [] #uniqe characters of all words
    length = 0 #lenght of characters of all words
    for word in data:
        ch += list(set(word))
        length += len(word)
    
    ch = list(set(ch))
    sample = int(round(length * (p / 100.0)))
    w = []
    
    while sample:
        sample = sample - 1
        i = random.randint(1, len(data)-1)
        chars = list(data[i])
        w[:] = []
        for char in chars:
            j = random.randint(1, len(ch)-1) #random word index
            char = ch[j]
            w.append(char)
        data[i] = ''.join(w)
    return data

'''
----------------------------------------------------------------
2. Cross-Entropy and Language Modeling
----------------------------------------------------------------
'''

def probAll(keys, nGrams, n):
    p = 0
    # nGrams = [uniGram, biGram, triGram]
    uniGram = nGrams[0]
    biGram = nGrams[1]
    triGram = nGrams[2]
    # keys = [word,prevWord1,prevWord2]
    word = keys[0] 
    prevWord1 = keys[1]
    prevWord2 = keys[2]
    
    biKey = word + "|" + prevWord1
    triKey = word + "|" + prevWord2 + " " + prevWord1
    
    if n > 0 and prevWord1 in uniGram and (prevWord1 + "|" + prevWord2) in biGram:
        if   n == 1: 
            p = 1.0 * uniGram[word]/(sum(uniGram.values())-1) if uniGram.has_key(word) else 0
        elif n == 2: 
            p = 1.0 * biGram[biKey] / uniGram[prevWord1] if biGram.has_key(biKey) else 0
        elif n == 3: 
            p = 1.0 * triGram[triKey] / biGram[prevWord1 + "|" + prevWord2] if triGram.has_key(triKey) else 0
    else:
        p = 1.0 / (len(uniGram)-1)
        
    return p



def probInt(keys, nGrams, l):
    iProb = l[0] * probAll(keys, nGrams, 0) + \
            l[1] * probAll(keys, nGrams, 1) + \
            l[2] * probAll(keys, nGrams, 2) + \
            l[3] * probAll(keys, nGrams, 3)
    return iProb


def crossEntropy(dataTest, dataTrain, l):
    sumProb = 0
    
    data = dataTest
    uniGram = nGram(dataTrain, 1)
    biGram = nGram(dataTrain, 2)
    triGram = nGram(dataTrain, 3)
    nGrams = [uniGram, biGram, triGram]
    
    prevWord1 = "<S>"
    prevWord2 = "<S>"
    for word in data:
        keys = [word,prevWord1,prevWord2]
        iProb = probInt(keys, nGrams, l)
        
        prevWord2 = prevWord1
        prevWord1 = word
        
        sumProb += math.log(iProb,2)
    
    H = -1.0 * sumProb / len(data)
    
    return H


def trainLambda(dataTest, dataTrain, l):
    newl = [0, 0, 0, 0]
    
    data = dataTest
    uniGram = nGram(dataTrain, 1)
    biGram = nGram(dataTrain, 2)
    triGram = nGram(dataTrain, 3)
    nGrams = [uniGram, biGram, triGram]
    
    prevWord1 = "<S>"
    prevWord2 = "<S>"
    # expected counts calculations
    for word in data:
        keys = [word,prevWord1,prevWord2]
        
        newl[0] += 1.0 * probAll(keys, nGrams, 0) / probInt(keys, nGrams, l)
        newl[1] += 1.0 * probAll(keys, nGrams, 1) / probInt(keys, nGrams, l)
        newl[2] += 1.0 * probAll(keys, nGrams, 2) / probInt(keys, nGrams, l)
        newl[3] += 1.0 * probAll(keys, nGrams, 3) / probInt(keys, nGrams, l)

        prevWord2 = prevWord1
        prevWord1 = word
    # next lambda calculations     
    for i in range(len(newl)):
        newl[i] *= l[i]    
    sumNewl = sum(newl)
    
    for i in range(len(newl)):
        newl[i] /= sumNewl
    
    return newl

def testLambda(newl, l, epsilon = 0.001):
    # test if next lambda and current lambda has difference less than epsilon
    for i in range(len(newl)):
        test = False if (abs(l[i] - newl[i]) > epsilon) else True
        
    return test