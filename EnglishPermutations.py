

def englishperms(x):
    from nltk.corpus import words
    from itertools import permutations
    out=[]
    permutationlist=[''.join(p) for p in permutations(x)]
    for term in permutationlist:
        if term in words.words():
            if term not in out:
                out+=[term]
    return out
