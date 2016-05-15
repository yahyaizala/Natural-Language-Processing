from nltk import CFG
gramer=CFG.fromstring("""
    S ->NP VP
    VP ->V NP
    V -> "eats"|"drinks"
    NP ->DET N
    Det ->"a"| "an" |"the"
    N ->"president"|"obama"|"apple"|"coke"
    """)
print gramer.productions()