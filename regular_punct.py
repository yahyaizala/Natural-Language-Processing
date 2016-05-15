from Utils import getDataManual,getManual
from nltk.tokenize import regexp_tokenize,wordpunct_tokenize
data=getDataManual()
rg=regexp_tokenize(data, pattern="\w+")
print rg
wt=wordpunct_tokenize(data)
print wt



