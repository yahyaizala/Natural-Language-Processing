#-*- coding:utf-8 -*-
from nltk import sent_tokenize,word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from csv import reader
def preprocessing(text):
    text=text.decode("utf-8")
    tokens=[w for sent in sent_tokenize(text) for w in word_tokenize(sent)]
    stop=stopwords.words("english")
    tokens=[token.lower() for token in tokens if token not in stop and token.__len__()>=3]
    stemer=WordNetLemmatizer()
    tokens=[stemer.lemmatize(word) for word in tokens]
    txt=" ".join(tokens)
    return txt

data=reader(open("data/SMSSpamCollection"),delimiter='\t')
sms=labels=[]
for line in data:
    labels.append(line[0])
    sms.append(preprocessing(line[1]))
data.close()






