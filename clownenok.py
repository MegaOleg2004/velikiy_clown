import pickle
from datasets import load_dataset
import re
from collections import defaultdict
word_count = defaultdict(int)
data = []
input_data_summary = []
output_data_summary = []
dataset = load_dataset("gigaword")
print("Document:", dataset["train"][0]["document"])
print("Title:", dataset["train"][0]["summary"])
for i in range(3500000):
    input_data_summary.append(dataset['train'][i]['document'])
    output_data_summary.append(dataset['train'][i]['summary'])
print(input_data_summary[0])
print(input_data_summary[1])
text = ''
for i in range(0, 500000):
    text += input_data_summary[i] + output_data_summary[i]
    print(i)
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
with open('word_count_last.pkl', 'wb') as f:
    pickle.dump(sorted_word_count, f)