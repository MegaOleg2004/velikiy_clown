import pickle
from collections import defaultdict

with open('word_count_last.pkl', 'rb') as f:
    sorted_word_count = pickle.load(f)
kolvo = 0
ultraslovar = []
print(len(sorted_word_count))
for word, count in sorted_word_count.items():
    if kolvo == 15001:
        word = 'NONE'
        ultraslovar.append(word)
        break
    if all(char not in word for char in (';', ')', '»', '«', '·', '“', "'")):
        kolvo += 1
        ultraslovar.append(word)

with open('ultraslovar_last.pkl', 'wb') as f:
    pickle.dump(ultraslovar, f)

print(kolvo)