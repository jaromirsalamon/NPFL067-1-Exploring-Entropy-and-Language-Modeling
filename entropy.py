import npfl067

lines_ref = [record.strip() for record in open('TEXTEN1.txt', 'r')]
lines_ref[-1] = "<S>"

p = [0, 0.001, 0.01, 0.1, 1, 5, 10, 20]

H = []
uni_gram = {}
bi_gram = {}
lines = []

print 'probability\tmin(H)\tavg(H)\tmax(H)\tperplexity'
for px in p:    
    H[:] = []
    for i in range(10):
        lines = npfl067.replaceWords(lines_ref,px)
        uni_gram = npfl067.nGram(lines,1)
        bi_gram = npfl067.nGram(lines,2)
    
        H.append(npfl067.condEntropy(uni_gram, bi_gram))

    print px,'\t','{0:.4f}'.format(min(H)),'\t','{0:.4f}'.format(sum(H) / len(H)),'\t','{0:.4f}'.format(max(H)),'\t','{0:.4f}'.format(2**(sum(H) / len(H)))

uni_gram.clear()
bi_gram.clear()
lines[:] = []
lines_ref = [record.strip() for record in open('TEXTEN1.txt', 'r')]
lines_ref[-1] = "<S>"

print 'probability\tmin(H)\tavg(H)\tmax(H)\tperplexity'
for px in p:    
    H[:] = []
    for i in range(10):
        lines = npfl067.replaceChars(lines_ref,px)
        uni_gram = npfl067.nGram(lines,1)
        bi_gram = npfl067.nGram(lines,2)
    
        H.append(npfl067.condEntropy(uni_gram, bi_gram))

    print px,'\t','{0:.4f}'.format(min(H)),'\t','{0:.4f}'.format(sum(H) / len(H)),'\t','{0:.4f}'.format(max(H)),'\t','{0:.4f}'.format(2**(sum(H) / len(H)))
    
uni_gram.clear()
bi_gram.clear()
lines[:] = []
lines_ref = [record.strip() for record in open('TEXTCZ1.txt', 'r')]
lines_ref[-1] = "<S>"

print 'probability\tmin(H)\tavg(H)\tmax(H)\tperplexity'
for px in p:    
    H[:] = []
    for i in range(10):
        lines = npfl067.replaceWords(lines_ref,px)
        uni_gram = npfl067.nGram(lines,1)
        bi_gram = npfl067.nGram(lines,2)
    
        H.append(npfl067.condEntropy(uni_gram, bi_gram))

    print px,'\t','{0:.4f}'.format(min(H)),'\t','{0:.4f}'.format(sum(H) / len(H)),'\t','{0:.4f}'.format(max(H)),'\t','{0:.4f}'.format(2**(sum(H) / len(H)))
    
uni_gram.clear()
bi_gram.clear()
lines[:] = []
lines_ref = [record.strip() for record in open('TEXTCZ1.txt', 'r')]
lines_ref[-1] = "<S>"

print 'probability\tmin(H)\tavg(H)\tmax(H)\tperplexity'
for px in p:    
    H[:] = []
    for i in range(10):
        lines = npfl067.replaceChars(lines_ref,px)
        uni_gram = npfl067.nGram(lines,1)
        bi_gram = npfl067.nGram(lines,2)
    
        H.append(npfl067.condEntropy(uni_gram, bi_gram))

    print px,'\t','{0:.4f}'.format(min(H)),'\t','{0:.4f}'.format(sum(H) / len(H)),'\t','{0:.4f}'.format(max(H)),'\t','{0:.4f}'.format(2**(sum(H) / len(H)))

uni_gram.clear()
bi_gram.clear()
lines[:] = []
lines_ref_en = [record.strip() for record in open('TEXTEN1.txt', 'r')]
lines_ref_cz = [record.strip() for record in open('TEXTCZ1.txt', 'r')]
lines_ref = ["<S>"]
lines_ref = lines_ref_en + lines_ref_cz

print 'probability\tmin(H)\tavg(H)\tmax(H)\tperplexity'
for px in p:    
    H[:] = []
    for i in range(10):
        lines = npfl067.replaceWords(lines_ref,px)
        uni_gram = npfl067.nGram(lines,1)
        bi_gram = npfl067.nGram(lines,2)
    
        H.append(npfl067.condEntropy(uni_gram, bi_gram))

    print px,'\t','{0:.4f}'.format(min(H)),'\t','{0:.4f}'.format(sum(H) / len(H)),'\t','{0:.4f}'.format(max(H)),'\t','{0:.4f}'.format(2**(sum(H) / len(H)))

uni_gram.clear()
bi_gram.clear()
lines[:] = []
lines_ref_en = [record.strip() for record in open('TEXTEN1.txt', 'r')]
lines_ref_cz = [record.strip() for record in open('TEXTCZ1.txt', 'r')]
lines_ref = ["<S>"]
lines_ref = lines_ref_en + lines_ref_cz

print 'probability\tmin(H)\tavg(H)\tmax(H)\tperplexity'
for px in p:    
    H[:] = []
    for i in range(10):
        lines = npfl067.replaceChars(lines_ref,px)
        uni_gram = npfl067.nGram(lines,1)
        bi_gram = npfl067.nGram(lines,2)
    
        H.append(npfl067.condEntropy(uni_gram, bi_gram))

    print px,'\t','{0:.4f}'.format(min(H)),'\t','{0:.4f}'.format(sum(H) / len(H)),'\t','{0:.4f}'.format(max(H)),'\t','{0:.4f}'.format(2**(sum(H) / len(H)))
