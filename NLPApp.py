from operator import itemgetter
from nltk import pos_tag,ne_chunk
from nltk import sent_tokenize,word_tokenize
f=open("dosya.txt","r")
data=f.read()
res=[]
for numb,sent in enumerate(sent_tokenize(data)):
    token_cnt=len(word_tokenize(sent))
    tagged=pos_tag(word_tokenize(sent))
    nouns=[w for w,tgd in tagged if tgd in ["NN","NNP"]]
    cnouns=len(nouns)
    ners=ne_chunk(pos_tag(word_tokenize(sent)),binary=False)
    cners=len([w for w in ners if hasattr(w,'node')])
    score=(cners+cnouns)/float(token_cnt)
    res.append((numb,token_cnt,cners,cnouns,score,sent))
for s in sorted(res,key=itemgetter(4),reverse=True):
    print s[5]

