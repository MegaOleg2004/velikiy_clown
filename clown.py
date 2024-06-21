import pymorphy2
from gensim.models import Word2Vec

morph = pymorphy2.MorphAnalyzer()
VECTOR = Word2Vec.load("oleg.bin")
print(VECTOR.wv.most_similar('странный', topn = 5))
similarity = VECTOR.wv.similarity('сунь', 'укун')
print(VECTOR.wv.get_vector("клоун"))
print({similarity})

