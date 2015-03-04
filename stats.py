import npfl067

lines_ref = [record.strip() for record in open('TEXTEN1.txt', 'r')]
lines_ref[-1] = "<S>"

uni_gram = npfl067.nGram(lines_ref,1)
bi_gram = npfl067.nGram(lines_ref,2)

print 'unigram counts:',len(uni_gram)
print 'bigram counts:',len(bi_gram)

lines_ref = [record.strip() for record in open('TEXTCZ1.txt', 'r')]
lines_ref[-1] = "<S>"

uni_gram = npfl067.nGram(lines_ref,1)
bi_gram = npfl067.nGram(lines_ref,2)

print 'unigram counts:',len(uni_gram)
print 'bigram counts:',len(bi_gram)

lines_ref_en = [record.strip() for record in open('TEXTEN1.txt', 'r')]
lines_ref_cz = [record.strip() for record in open('TEXTCZ1.txt', 'r')]
lines_ref = ["<S>"]
lines_ref = lines_ref_en + lines_ref_cz

uni_gram = npfl067.nGram(lines_ref,1)
bi_gram = npfl067.nGram(lines_ref,2)

print 'unigram counts:',len(uni_gram)
print 'bigram counts:',len(bi_gram)