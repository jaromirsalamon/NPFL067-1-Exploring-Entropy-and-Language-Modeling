import npfl067
from timer import Timer

linesRef = [record.strip() for record in open('TEXTEN1.txt', 'r')]

trainData = linesRef[0:len(linesRef)-60000]
#trainData = linesRef[0:10]
print 'train data length',len(trainData)

heldData = linesRef[-60000:-20000]
#heldData = linesRef[10:20]
print 'held data length',len(heldData)

testData = linesRef[-20000:len(linesRef)]
#testData = linesRef[20:30]
print 'test data length',len(testData)

with Timer() as t:
    uniGram = npfl067.nGram(trainData, 1)
print "=> elasped uniGram: %s s" % t.secs

with Timer() as t:
    biGram = npfl067.nGram(trainData, 2)
print "=> elasped biGram: %s s" % t.secs

with Timer() as t:
    triGram = npfl067.nGram(trainData, 3)
print "=> elasped triGram: %s s" % t.secs

l = [0.25, 0.25, 0.25, 0.25]

data = trainData
nGrams = [uniGram, biGram, triGram]
prevWord1 = "<S>"
prevWord2 = "<S>"
for word in data:
    keys = [word,prevWord1,prevWord2]
    
    with Timer() as t:
        iProb = npfl067.probInt(keys, nGrams, l)
    print "=> elasped interpolated probability: %s s" % t.secs

    iProb = 0
    with Timer() as t:
        iProb += l[0] * npfl067.probAll(keys, nGrams, 0)
    print "=> elasped probability 1: %s s" % t.secs
    with Timer() as t:
        iProb += l[1] * npfl067.probAll(keys, nGrams, 1)
    print "=> elasped probability 2: %s s" % t.secs
    with Timer() as t:
        iProb += l[2] * npfl067.probAll(keys, nGrams, 2)
    print "=> elasped probability 3: %s s" % t.secs
    with Timer() as t:
        iProb += l[3] * npfl067.probAll(keys, nGrams, 3)
    print "=> elasped probability 4: %s s" % t.secs

    prevWord2 = prevWord1
    prevWord1 = word

with Timer() as t:
    H = npfl067.crossEntropy(testData,trainData, l)
print "=> elasped crossEntropy: %s s" % t.secs
print H
