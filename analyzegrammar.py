#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:58:02 2017

@author: stechen1
"""
import csv
import spacy
nlp = spacy.load('en')
from processtext import *

noun=0
verb=0
adjective=0

verbs={}
nouns={}
adjectives={}

filename='yankeeinput’

def updatedict(word,dictionary):
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
        
with open(filename + '.txt', encoding='utf-8') as old:
    for line in old:      
        line=cleanstring(cleanemoji(line))
        cleanline=nlp(line)
        for word in cleanline:
            if word.pos_=='VERB' and len(word.lemma_)>2:
                updatedict(word.lemma_,verbs)
                verb+=1
            elif word.pos_=='NOUN' and len(word.lemma_)>2:
                updatedict(word.lemma_,nouns)
                noun+=1
            elif word.pos_=='ADJ' and word.lemma_!='-PRON-':
                updatedict(word.lemma_,adjectives)
                adjective+=1
                
## write results
with open(filename + '_nouns.csv','w') as n:
    for k,v in nouns.items():
        n.write(k + ',' + str(v) + '\n')
        
with open(filename + '_verbs.csv','w') as b:
    for k,v in verbs.items():
        b.write(k + ',' + str(v) + '\n')
        
with open(filename + '_adjectives.csv','w') as j:
    for k,v in adjectives.items():
        j.write(k + ',' + str(v) + '\n')

print ('adjectives: ' + str(adjective) + ' nouns: ' + str(noun) + ' verbs: ' + str(verb))
