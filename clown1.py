import json, time, pymorphy2
from gensim.utils import simple_preprocess
from gensim.models import Word2Vec

morph = pymorphy2.MorphAnalyzer()
VECTOR = Word2Vec.load("oleg.bin")

tokenized = []

def all_comments(text):
    global tokenized
    for comment in text.split("."):
        tokenized.append(simple_preprocess(comment, deacc = False, min_len = 2))
    print(tokenized[0], tokenized[1])

with open("TEXT.txt", encoding = 'utf-8') as f:
    s = f.read()

all_comments(s)

#normal = tokenized.copy()
#for i in range (len(tokenized)):
    #if len(tokenized[i]) != 0:
        #for j in range(len(tokenized[i])):
            #if len(tokenized[i][j]) != 0:
                #normal[i][j] = morph.parse(tokenized[i][j])[0].normal_form

VECTOR.build_vocab(tokenized, update=True)
VECTOR.train(tokenized, total_examples=VECTOR.corpus_count, epochs=4)

VECTOR.save("oleg.bin")
