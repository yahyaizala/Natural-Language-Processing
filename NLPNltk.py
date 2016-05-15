import nltk
from sklearn.feature_extraction.text import  TfidfVectorizer
from Utils import getDataFile
ew=[]
f=getDataFile()
sents=nltk.sent_tokenize(f)
vec=TfidfVectorizer(min_df=0,use_idf=True
                    ,smooth_idf=False,sublinear_tf=True)
skle=vec.fit_transform(sents)
print skle.toarray()
for d in skle.toarray():
    ew.append(d.sum()/float(len(d.nonzero()[0])))
print ew