'''DICT DEMOSTRATION'''
import re
sts="pythonic way! the easiest way to implementing amazing things!"
print  re.findall("!",sts)
#   ['!', '!']
if re.search("!",sts):
    print "fine"
else:
    print "not found"
freq={}
tokens=sts.replace("!","").split()
for token in tokens:
    if token in freq:
        freq[token] +=1
    else:
        freq[token]=1
print  freq

