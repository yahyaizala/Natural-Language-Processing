'''LISTS DEMOSTRATION'''
list=[4,5,6,7]
print list
print list[0]
print list[-1]
print list[:2]
#print dir(list)
list.append(12)
print  list
alist=[4,5,6]
list.extend(alist)
print  list
uw=list.index(12)
print  uw

strs="yahya! ali computer? engineer\n\r"
print strs
strs=strs.strip()
print  strs
strs=strs.replace("!","").replace("?","")
strs=strs.split()
print  strs


