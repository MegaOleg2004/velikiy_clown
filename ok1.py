import json, gzip
import pickle
import re
from collections import defaultdict
word_count = defaultdict(int)
path = "D:/Олег 3/release/test.jsonl.gz"
data = []
input_data_summary = []
output_data_summary = []

with gzip.open(path) as f:
    for ln in f:
        obj = json.loads(ln)
        data.append(obj)

for i in range(len(data)):
    input_data_summary.append(data[i]['summary'])
    output_data_summary.append(data[i]['title'])
print(input_data_summary[0])
print(input_data_summary[1])
text = ''
for i in range(0, len(data)):
    text += input_data_summary[i] + output_data_summary[i]
    print(i)
print(text)
k = 0
words = text.split()
for word in words:
    k = k + 1
    if not re.search(r'\d', word):
        if word[len(word) - 1] in '!,"$@*^/():.|?»-+#':
            if len(word) == 1:
                continue
            word = word[0:len(word) - 1]
        if word[0] in '!,"$@*^/():.|?«-+#':
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

