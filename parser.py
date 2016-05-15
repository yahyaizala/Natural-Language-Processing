from nltk.chunk.regexp import *
from  nltk import pos_tag
from nltk.tokenize import word_tokenize
rules=ChunkRule("<.*>+","chunk everything")
reg=RegexpParser("""
NP :{<DT>?<JJ> *<NN>*}
P:{<IN>}
V:{<V.*>}
PP:{<P><NP>}
VP:{<V><NP|PP>*}
""")
test="Mr. Obama player a big role in the insurance bill"
test_pos=pos_tag(word_tokenize(test))
parsed=reg.parse(test_pos)
print parsed