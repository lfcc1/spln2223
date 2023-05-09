#!/usr/bin/env python3
import spacy
import sys
from collections import Counter
import argparse

parser = argparse.ArgumentParser(
    prog= 'Verb Ratio',
    description= 'Generates a list of occurences of the verbs captured from a text divided by the the number of occurences from a list of lemmas, finally it writes the list to stdout',
    epilog= 'Made for SPLN 2022/2023'
)

parser.add_argument('--file', '-f', help="Define the file that contains the lemmas of verbs from a big corpus of information", required=True)

parser.add_argument('--sort', '-s', help="Sorts the ratios", required=False, action='store_true')
args = parser.parse_args()

nlp = spacy.load("pt_core_news_lg")
#nlp = pt_core_news_md.load()
text = '''
O José Pedro da Silva está a fazer piloto de teste na cidade de Braga.
O Igor Viana está a fazer de copiloto de teste na cidade de Braga.
'''

text = sys.stdin.read()

doc = nlp(text)
dict = Counter()
for w in doc:
    if w.pos_ == "VERB":
        dict[w.lemma_] += 1
    #print(w, w.pos_, w.lemma_, w.ent_iob_, w.ent_type_)

dict_norm = Counter()
for key, value in dict.items():
    if value >=  5:
        dict_norm[key] += value

#for s in doc.sents:
#    for ent in s.ents:
#        dict[ent.orth_] += 1

lemas = open(args.file, "r")

dict_lema = Counter()
for line in lemas:
    campos = line.split()
    if len(campos) >= 2:
        dict_lema[campos[1]] = int(campos[0])

dict_ratio = {}
for verb, value in dict_norm.items():
    dict_ratio[verb] = value/dict_lema.get(verb,100)

if args.sort:
    it = sorted(dict_ratio.items(), key = lambda x:x[1])
else:
    it = dict_ratio.items()
for verb, value in it:
    print(f'{value:.20f}', verb)
