from nltk.tokenize import word_tokenize
from nltk.corpus import brown
import nltk
from nltk import ne_chunk
#train=brown.sents()[:int(len(brown.sents())*0.7)]
#test=brown.sents()[int(len(brown.sents())*0.2)]
s="yahya kesenek a studient at stanford university"
print ne_chunk(nltk.pos_tag(word_tokenize(s)))




