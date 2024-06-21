import pickle
import numpy as np
import json, gzip

path = "D:/Олег 3/release/train.jsonl.gz"

with open('ultraslovar1.pkl', 'rb') as f:
    ultraslovar = pickle.load(f)

k = 0

massiv1 = []
massiv2 = []
data = []
input_data_summary = []
output_data_summary = []

with gzip.open(path) as f:
    for ln in f:
        obj = json.loads(ln)
        data.append(obj)

for i in range(len(data)):
    input_data_summary.append(data[i]['text'])
    output_data_summary.append(data[i]['title'])
print(input_data_summary[2])
for i in range(len(data)):
    print(i)
    text1 = input_data_summary[i]
    text2 = output_data_summary[i]
    words1 = text1.split()
    words2 = text2.split()
    part_of_massiv1 = []
    part_of_massiv2 = []
    k1 = 0
    k2 = 0
    for word in words1:
        word = word.lower()
        if word[len(word) - 1] in '!,"$@*^/():.|?»-+':
            if len(word) == 1:
                continue
            word = word[0:len(word) - 1]
        if word[0] in '!,"$@*^/():.|?«-+':
            if len(word) == 1:
                continue
            word = word[1:len(word)]
        if k1 == 90:
            break
        if word in ultraslovar:
            part_of_massiv1.append(ultraslovar.index(word))
            k1 += 1
    if k1 < 90:
        part_of_massiv1.extend([12001] * (90 - len(part_of_massiv1)))
    massiv1.append(part_of_massiv1)
    for word in words2:
        word = word.lower()
        if word[len(word) - 1] in '!,"$@*^/():.|?»-+':
            if len(word) == 1:
                continue
            word = word[0:len(word) - 1]
        if word[0] in '!,"$@*^/():.|?«-+':
            if len(word) == 1:
                continue
            word = word[1:len(word)]
        if k2 == 10:
            break
        if word in ultraslovar:
            part_of_massiv2.append(ultraslovar.index(word))
            k2 += 1
    if k2 < 10:
        part_of_massiv2.extend([12001] * (10 - len(part_of_massiv2)))
    massiv2.append(part_of_massiv2)

np.savetxt("input_data_summary_last.txt", massiv1, fmt="%d")
np.savetxt("output_data_summary_last.txt", massiv2, fmt="%d")






