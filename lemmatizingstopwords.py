#-*- coding:utf-8 -*-
from Utils import getQues,to_turkish
from nltk.corpus import stopwords
from nltk import FreqDist
stop=stopwords.words("turkish")
face=getQues()
face=face.split()
tokens=[token for token in face if token not in stop]
fqs=FreqDist(tokens)
low=fqs.keys()[-10:]
tokens=[token for token in tokens if token not in low]
print tokens
