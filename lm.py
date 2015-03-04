import npfl067
import decimal
decimal.getcontext().prec = 15

linesRef = [record.strip() for record in open('TEXTCZ1.txt', 'r')]

trainData = linesRef[0:len(linesRef)-60000]
#trainData = linesRef[0:10]
print 'train data length',len(trainData)

heldData = linesRef[-60000:-20000]
#heldData = linesRef[10:20]
print 'held data length',len(heldData)

testData = linesRef[-20000:len(linesRef)]
#testData = linesRef[20:30]
print 'test data length',len(testData)

uniGram = npfl067.nGram(trainData, 1)
biGram = npfl067.nGram(trainData, 2)
triGram = npfl067.nGram(trainData, 3)

print 'vocabulary size:',(len(uniGram)-1)

#initial setup of lambdas
l = [0.25, 0.25, 0.25, 0.25]
#initial setup of new lambdas
newl = [0, 0, 0, 0]
#setup of epsilon
e = 0.001

iteration = 0
print 'iteration\tlambdas\tcross entropy'
H = npfl067.crossEntropy(trainData, trainData, l)
print iteration,'\t',l,'\t',H

# Train lambdas using train data
while True:
    iteration += 1
    newl = npfl067.trainLambda(trainData, trainData, l)
    H = npfl067.crossEntropy(trainData, trainData, newl)
    print iteration,'\t',newl,'\t',H
    if (npfl067.testLambda(newl, l, e)):
        l = newl
        break
    l = newl

# Final calculation of cross entropy using test data and lambda calculated from train data
H = npfl067.crossEntropy(testData, trainData, l) 
print 'F\t',l,'\t',H

iteration = 0
print 'iteration\tlambdas\tcross entropy'
H = npfl067.crossEntropy(heldData, trainData, l)
print iteration,'\t',l,'\t',H

# Train lambdas using held out data
while True:
    iteration += 1
    newl = npfl067.trainLambda(heldData, trainData, l)
    H = npfl067.crossEntropy(heldData, trainData, newl)
    print iteration,'\t',newl,'\t',H
    if (npfl067.testLambda(newl, l, e)):
        l = newl
        break
    l = newl

# Calculate cross entropy using test data and lambda calculated from held data
H = npfl067.crossEntropy(testData,trainData, l)
print 'F\t',l,'\t',H

#tweaking lambda 3
# add 10%, 20%, 30%, ..., 90%, 95% and 99% of the difference between the tri-gram smoothing parameter and 1.0 to its value
prop1 = [.10, .20, .30, .40, .50, .60, .70, .80, .90, .95, .99]
# then set the trigram smoothing parameter to 90%, 80%, 70%, ... 10%, 0% of its value
prop2 = [.90, .80, .70, .60, .50, .40, .30, .20, .10, 0]

print 'proportion\tl[0]\tl[1]\tl[2]\tl[3]\tcross entropy'
print '100%\t','{0:.4f}'.format(l[0]),'\t','{0:.4f}'.format(l[1]),'\t','{0:.4f}'.format(l[2]),'\t','{0:.4f}'.format(l[3]),'\t',H

l3 = 0
print 'proportion\tl[0]\tl[1]\tl[2]\tl[3]\tcross entropy'
for i in range(len(prop1)):
    l3 = (1 - l[3]) * prop1[i]
    r = (1 - l3)/(1-l[3])
    newl = [l[0] * r, l[1] * r, l[2] * r, l3]
    H = npfl067.crossEntropy(testData, trainData, newl)
    print prop1[i] * 100,'%\t','{0:.4f}'.format(newl[0]),'\t','{0:.4f}'.format(newl[1]),'\t','{0:.4f}'.format(newl[2]),'\t','{0:.4f}'.format(newl[3]),'\t',H

print 'proportion\tl[0]\tl[1]\tl[2]\tl[3]\tcross entropy'
for i in range(len(prop2)):
    l3 = l[3] * prop2[i]
    r = (1 - l3)/(1-l[3])
    newl = [l[0] * r, l[1] * r, l[2] * r, l3]
    npfl067.crossEntropy(testData, trainData, newl)
    print prop2[i] * 100,'%\t','{0:.4f}'.format(newl[0]),'\t','{0:.4f}'.format(newl[1]),'\t','{0:.4f}'.format(newl[2]),'\t','{0:.4f}'.format(newl[3]),'\t',H
