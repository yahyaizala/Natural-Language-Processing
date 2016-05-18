from  __future__ import division
from nltk.corpus import names
from nltk.classify import NaiveBayesClassifier
from random import randrange
def shuffle(cits):
    _len = len(cits)
    for a in range(_len):
        temp = cits[a]
        idx = randrange(0, _len)
        cits[a] = cits[idx]
        cits[idx] = temp
def gender(word):
    return {"info":word[-1]}
males=[(name,'male') for name in names.words("male.txt")]
females=[(name,'female') for name in names.words("female.txt")]
cits=(males+females)
shuffle(cits)
features=[(gender(w),g) for (w,g) in cits]
train,test=features[500:],features[:500]
clf=NaiveBayesClassifier.train(train)
print clf.classify(gender("ali"))
'''
print features[:10]
[({'info': u'a'}, 'female'),
({'info': u'e'}, 'female'),
({'info': u's'}, 'male'),
({'info': u'a'}, 'female'),
({'info': u'y'}, 'male'),
({'info': u'e'}, 'female'),
({'info': u'a'}, 'female'),
({'info': u'g'}, 'male'),
({'info': u'a'}, 'female'),
 ({'info': u'a'}, 'female')]

'''



#feature=[(gender(n),g) for (n,g) in _names]
#print feature[:10]