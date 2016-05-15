#-*- coding:utf-8 -*-
from nltk.tokenize import sent_tokenize
from nltk.tokenize.punkt import  PunktSentenceTokenizer
from Utils import getManual
sent=getManual()
tokens=sent_tokenize(sent)
print  tokens
punk=PunktSentenceTokenizer()
pun=punk.tokenize(sent.strip())
print pun