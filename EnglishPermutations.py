#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 12:32:24 2017
this gives the seven letter word in that game
@author: pi314
"""

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
