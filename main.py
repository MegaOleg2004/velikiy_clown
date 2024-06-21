from datasets import load_dataset
import pickle
import re
from collections import defaultdict
dataset = load_dataset('oscar', "unshuffled_deduplicated_ru", split='train', streaming=True) # streaming=True
word_count = defaultdict(int)
it = iter(dataset)
k = 0
while k < 1000000000:
    print(k)
    text = next(it)['text']
    k = k + len(text)
    words = text.split()
    for word in words:
        if not re.search(r'\d', word):
            if word[len(word) - 1] in '!,"$@*^/():.|?»-+':
                if len(word) == 1:
                    continue
                word = word[0:len(word) - 1]
            if word[0] in '!,"$@*^/():.|?«-+':
                if len(word) == 1:
                    continue
                word = word[1:len(word)]
            word = word.lower()
            word_count[word] += 1
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
for word, count in sorted_word_count.items():
    print(word, count)
with open('word_count.pkl', 'wb') as f:
    pickle.dump(sorted_word_count, f)