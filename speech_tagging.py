from nltk import pos_tag,word_tokenize
#from Utils import getQues
#txt=getQues()
#txt="benim adim yahya"
from nltk.tag.stanford import StanfordPOSTagger
txt="i am dentist"
tgr=StanfordPOSTagger('models/english-bidirectional-distdim.tagger','standford-postagger.jar')
print  tgr.tag(word_tokenize(txt))