from sklearn.metrics import confusion_matrix,classification_report
import numpy as np
from ClfUtisl import PreProcessor
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
data,tags=PreProcessor().getData()
len_sms=int(round(len(data)*0.7))
x_train=np.array([''.join(sm) for sm in data[:len_sms]])
y_train=np.array([sm for sm in tags[:len_sms]])
x_test=np.array([''.join(sm) for sm in data[len_sms + 1:]])
y_test=np.array([sm for sm in tags[len_sms + 1:]])
victor=TfidfVectorizer(ngram_range=(1,2),stop_words="english",min_df=1,strip_accents="unicode")
Xtrain=victor.fit_transform(x_train)
Xtest=victor.transform(x_test)
'''Desicion Tree
dclf=DecisionTreeClassifier().fit(Xtrain.toarray(),y_train)
y_pred=dclf.predict(Xtest.toarray())
print y_pred
'''
'''SGD or MaxEnt'''
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import classification_report
maxent=SGDClassifier(alpha=0.001,n_iter=50).fit(Xtrain,y_train)
m_pred=maxent.predict(Xtest)
print classification_report(y_test,m_pred)
'''LinearSVC'''
from sklearn.svm import LinearSVC
svc=LinearSVC().fit(Xtrain,y_train)
s_pred=svc.predict(Xtest)
print s_pred
print classification_report(y_test,s_pred)
'''Random Forest'''

