from nltk.tokenize import word_tokenize
from Utils import getManual,getDataManual,getData
data=getData()
words=word_tokenize(data)
print words