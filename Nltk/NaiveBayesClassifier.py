from  __future__ import division
from nltk.corpus import names
from nltk.classify import accuracy
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
def improvment(word):
    ftr={}
    ftr["fs"]=word[0].lower()
    ftr["ls"]=word[-1].lower()
    for letter in "abcdefghijklmnouprstuvyzwq":
        ftr["count(%s)"%letter]=word.lower().count(letter)
        ftr["has(%s)" %letter]=(letter in word.lower())
    return ftr
males=[(name,'male') for name in names.words("male.txt")]
females=[(name,'female') for name in names.words("female.txt")]
cits=(males+females)
shuffle(cits)
features=[(improvment(w),g) for (w,g) in cits]
train,test=features[500:],features[:500]
clf=NaiveBayesClassifier.train(train)
print train[:10]
'''
[
(
{'count(u)': 0, 'has(d)': False, 'count(b)': 1, 'count(w)': 0, 'has(b)': True, 'count(l)': 2, 'count(q)': 0,
'count(n)': 0, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': False, 'count(j)': 0,
 'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': False, 'has(u)': False,
  'count(d)': 0, 'has(t)': False, 'ls': u'e', 'has(s)': False, 'count(f)': 0, 'has(q)': False,
  'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 0, 'fs': u'b', 'has(c)': False,
   'count(v)': 0, 'count(m)': 0, 'has(a)': False, 'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': False,
   'count(i)': 0, 'has(r)': False, 'has(g)': False, 'count(k)': 0, 'count(y)': 0, 'has(n)': False, 'has(l)': True,
    'count(e)': 2, 'count(s)': 0, 'count(g)': 0, 'count(r)': 0, 'count(a)': 0, 'has(p)': False}, 'female'),
({'count(u)': 0, 'has(d)': False, 'count(b)': 0, 'count(w)': 0, 'has(b)': False, 'count(l)': 1, 'count(q)': 0,
'count(n)': 2, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': True, 'count(j)': 0,
'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': False, 'has(u)': False,
'count(d)': 0, 'has(t)': True, 'ls': u't', 'has(s)': False, 'count(f)': 0, 'has(q)': False,
'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 1, 'fs': u'l',
'has(c)': False, 'count(v)': 0, 'count(m)': 0, 'has(a)': False, 'has(v)': False,
 'count(p)': 0, 'count(o)': 0, 'has(i)': False, 'count(i)': 0, 'has(r)': False,
  'has(g)': False, 'count(k)': 0, 'count(y)': 1, 'has(n)': True, 'has(l)': True,
   'count(e)': 1, 'count(s)': 0, 'count(g)': 0, 'count(r)': 0, 'count(a)': 0, 'has(p)': False}, 'female'),
(
{'count(u)': 0, 'has(d)': False, 'count(b)': 0, 'count(w)': 0, 'has(b)': False, 'count(l)': 1, 'count(q)': 0,
'count(n)': 0, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': False, 'count(j)': 0,
'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': True, 'has(u)': False, 'count(d)': 0,
'has(t)': False, 'ls': u'l', 'has(s)': False, 'count(f)': 0, 'has(q)': False, 'has(w)': False, 'has(e)': True,
'has(z)': False, 'count(t)': 0, 'fs': u'k', 'has(c)': False, 'count(v)': 0, 'count(m)': 0, 'has(a)': False,
'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': True, 'count(i)': 1, 'has(r)': False, 'has(g)': False,
'count(k)': 1, 'count(y)': 0, 'has(n)': False, 'has(l)': True, 'count(e)': 1, 'count(s)': 0, 'count(g)': 0, 'count(r)': 0,
 'count(a)': 0, 'has(p)': False}, 'male'),

(
{'count(u)': 0, 'has(d)': False, 'count(b)': 0, 'count(w)': 0, 'has(b)': False, 'count(l)': 1, 'count(q)': 0, 'count(n)': 0, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': True, 'count(j)': 0, 'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': True, 'has(u)': False, 'count(d)': 0, 'has(t)': False, 'ls': u'e', 'has(s)': False, 'count(f)': 0, 'has(q)': False, 'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 0, 'fs': u'k', 'has(c)': False, 'count(v)': 0, 'count(m)': 0, 'has(a)': False, 'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': False, 'count(i)': 0, 'has(r)': False, 'has(g)': False, 'count(k)': 1, 'count(y)': 1, 'has(n)': False, 'has(l)': True, 'count(e)': 1, 'count(s)': 0, 'count(g)': 0, 'count(r)': 0, 'count(a)': 0, 'has(p)': False}, 'male'), ({'count(u)': 0, 'has(d)': False, 'count(b)': 0, 'count(w)': 1, 'has(b)': False, 'count(l)': 0, 'count(q)': 0, 'count(n)': 2, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': False, 'count(j)': 0, 'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': False, 'has(u)': False, 'count(d)': 0, 'has(t)': False, 'ls': u'e', 'has(s)': False, 'count(f)': 0, 'has(q)': False, 'has(w)': True, 'has(e)': True, 'has(z)': False, 'count(t)': 0, 'fs': u'g', 'has(c)': False, 'count(v)': 0, 'count(m)': 0, 'has(a)': False, 'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': True, 'count(i)': 1, 'has(r)': False, 'has(g)': True, 'count(k)': 0, 'count(y)': 0, 'has(n)': True, 'has(l)': False, 'count(e)': 2, 'count(s)': 0, 'count(g)': 1, 'count(r)': 0, 'count(a)': 0, 'has(p)': False}, 'female'), ({'count(u)': 0, 'has(d)': False, 'count(b)': 0, 'count(w)': 0, 'has(b)': False, 'count(l)': 0, 'count(q)': 0, 'count(n)': 1, 'has(j)': False, 'count(c)': 0, 'count(h)': 1, 'has(h)': True, 'has(y)': False, 'count(j)': 0, 'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': False, 'has(u)': False, 'count(d)': 0, 'has(t)': True, 'ls': u'e', 'has(s)': True, 'count(f)': 0, 'has(q)': False, 'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 1, 'fs': u's', 'has(c)': False, 'count(v)': 0, 'count(m)': 0, 'has(a)': False, 'has(v)': False, 'count(p)': 1, 'count(o)': 0, 'has(i)': True, 'count(i)': 1, 'has(r)': False, 'has(g)': False, 'count(k)': 0, 'count(y)': 0, 'has(n)': True, 'has(l)': False, 'count(e)': 3, 'count(s)': 1, 'count(g)': 0, 'count(r)': 0, 'count(a)': 0, 'has(p)': True}, 'female'), ({'count(u)': 0, 'has(d)': True, 'count(b)': 1, 'count(w)': 0, 'has(b)': True, 'count(l)': 0, 'count(q)': 0, 'count(n)': 1, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': False, 'count(j)': 0, 'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': False, 'has(u)': False, 'count(d)': 1, 'has(t)': False, 'ls': u'a', 'has(s)': False, 'count(f)': 0, 'has(q)': False, 'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 0, 'fs': u'b', 'has(c)': False, 'count(v)': 0, 'count(m)': 0, 'has(a)': True, 'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': False, 'count(i)': 0, 'has(r)': True, 'has(g)': False, 'count(k)': 0, 'count(y)': 0, 'has(n)': True, 'has(l)': False, 'count(e)': 1, 'count(s)': 0, 'count(g)': 0, 'count(r)': 1, 'count(a)': 2, 'has(p)': False}, 'female'), ({'count(u)': 0, 'has(d)': True, 'count(b)': 1, 'count(w)': 0, 'has(b)': True, 'count(l)': 0, 'count(q)': 0, 'count(n)': 2, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': False, 'count(j)': 0, 'has(f)': False, 'has(o)': False, 'has(m)': False, 'count(z)': 0, 'has(k)': False, 'has(u)': False, 'count(d)': 1, 'has(t)': False, 'ls': u'a', 'has(s)': False, 'count(f)': 0, 'has(q)': False, 'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 0, 'fs': u'b', 'has(c)': False, 'count(v)': 0, 'count(m)': 0, 'has(a)': True, 'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': True, 'count(i)': 1, 'has(r)': True, 'has(g)': False, 'count(k)': 0, 'count(y)': 0, 'has(n)': True, 'has(l)': False, 'count(e)': 1, 'count(s)': 0, 'count(g)': 0, 'count(r)': 2, 'count(a)': 2, 'has(p)': False}, 'female'), ({'count(u)': 0, 'has(d)': False, 'count(b)': 0, 'count(w)': 0, 'has(b)': False, 'count(l)': 1, 'count(q)': 0, 'count(n)': 0, 'has(j)': False, 'count(c)': 0, 'count(h)': 0, 'has(h)': False, 'has(y)': False, 'count(j)': 0, 'has(f)': False, 'has(o)': False, 'has(m)': True, 'count(z)': 0, 'has(k)': False, 'has(u)': False, 'count(d)': 0, 'has(t)': False, 'ls': u'l', 'has(s)': False, 'count(f)': 0, 'has(q)': False, 'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 0, 'fs': u'm', 'has(c)': False, 'count(v)': 0, 'count(m)': 1, 'has(a)': False, 'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': False, 'count(i)': 0, 'has(r)': False, 'has(g)': False, 'count(k)': 0, 'count(y)': 0, 'has(n)': False, 'has(l)': True, 'count(e)': 1, 'count(s)': 0, 'count(g)': 0, 'count(r)': 0, 'count(a)': 0, 'has(p)': False}, 'male'), ({'count(u)': 0, 'has(d)': False, 'count(b)': 0, 'count(w)': 0, 'has(b)': False, 'count(l)': 2, 'count(q)': 0, 'count(n)': 0, 'has(j)': False, 'count(c)': 1, 'count(h)': 1, 'has(h)': True, 'has(y)': False, 'count(j)': 0, 'has(f)': False, 'has(o)': False, 'has(m)': True, 'count(z)': 0, 'has(k)': False, 'has(u)': False, 'count(d)': 0, 'has(t)': True, 'ls': u'l', 'has(s)': False, 'count(f)': 0, 'has(q)': False, 'has(w)': False, 'has(e)': True, 'has(z)': False, 'count(t)': 1, 'fs': u'm', 'has(c)': True, 'count(v)': 0, 'count(m)': 1, 'has(a)': False, 'has(v)': False, 'count(p)': 0, 'count(o)': 0, 'has(i)': True, 'count(i)': 1, 'has(r)': False, 'has(g)': False, 'count(k)': 0, 'count(y)': 0, 'has(n)': False, 'has(l)': True, 'count(e)': 1, 'count(s)': 0, 'count(g)': 0, 'count(r)': 0, 'count(a)': 0, 'has(p)': False}, 'male')]



'''
print clf.classify(gender("john"))
print accuracy(clf,test)
fts2=[(improvment(w),g) for (w,g) in cits]
clf2=NaiveBayesClassifier.train(train)
print accuracy(clf2,test)

'''


'''




#female
#0.69

'''
clf.show_most_informative_features(15)

Most Informative Features
                    info = u'a'           female : male   =     36.9 : 1.0
                    info = u'k'             male : female =     31.8 : 1.0
                    info = u'f'             male : female =     15.5 : 1.0
                    info = u'p'             male : female =     11.4 : 1.0
                    info = u'v'             male : female =     10.7 : 1.0
                    info = u'm'             male : female =     10.4 : 1.0
                    info = u'd'             male : female =      9.7 : 1.0
                    info = u'o'             male : female =      8.6 : 1.0
                    info = u'r'             male : female =      7.2 : 1.0
                    info = u'z'             male : female =      5.7 : 1.0
                    info = u'g'             male : female =      5.2 : 1.0
                    info = u'b'             male : female =      4.4 : 1.0
                    info = u's'             male : female =      4.2 : 1.0
                    info = u't'             male : female =      4.1 : 1.0
                    info = u'j'             male : female =      4.0 : 1.0'''
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
