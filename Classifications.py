#-*- coding:utf-8 -*-
from nltk import sent_tokenize,word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import  CountVectorizer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix,classification_report
from csv import reader
import numpy as np
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
sms=[]
labels=[]
for line in data:
    labels.append(line[0])
    sms.append(preprocessing(line[1]))
len_sms_r=int(round(len(sms)*0.7))
len_sms=int(len(sms))
x_train=np.array([''.join(sm) for sm in sms[:len_sms_r]])
y_train=np.array([sm for sm in labels[:len_sms_r]])
x_test=np.array([''.join(sm) for sm in sms[len_sms_r+1:len_sms]])
y_test=np.array([sm for sm in labels[len_sms_r+1:len_sms]])
tfvic=TfidfVectorizer(min_df=1,ngram_range=(1,2),stop_words="english",strip_accents="unicode")
X_train=tfvic.fit_transform(x_train)
X_test=tfvic.transform(x_test)
clf=MultinomialNB().fit(X_train,y_train)
pred=clf.predict(X_test)
conmatrix=confusion_matrix(y_test,pred)
print conmatrix
print classification_report(y_test,pred)
'''
['ham' 'ham' 'ham' ..., 'ham' 'ham' 'ham']
[[1443    0]
 [  76  152]]
             precision    recall  f1-score   support

        ham       0.95      1.00      0.97      1443
       spam       1.00      0.67      0.80       228

avg / total       0.96      0.95      0.95      167


'''

'''
victor=CountVectorizer(min_df=1)
xp=victor.fit_transform(sms)
print "|".join(victor.get_feature_names())
print xp.toarray()[:3]

'''

'''
print sms
len_sms=int(round(len(sms)*0.7))
x_train=np.array([''.join(sm) for sm in sms[:len_sms]])
y_train=np.array([''.join(sm) for sm in sms[len_sms+1:]])
y_test=np.array([sm for sm in labels[len_sms+1:]] or sm in labels[len_sms+1:])
print "x train", x_train
print "y_train",y_train
print "y test",y_test
'''






