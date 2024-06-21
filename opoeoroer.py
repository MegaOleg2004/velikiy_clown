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

for i in range(3):
    input_data_summary.append(data[i]['summary'])
    output_data_summary.append(data[i]['title'])
for i in range(3):
    print('summary: ', input_data_summary[i])
    print('title: ', output_data_summary[i])
for i in range(3):
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
        if k1 == 80:
            break
        if word in ultraslovar:
            part_of_massiv1.append(ultraslovar.index(word))
            k1 += 1
    if k1 < 80:
        part_of_massiv1.extend([11501] * (80 - len(part_of_massiv1)))
    massiv1.append(part_of_massiv1)
    for word in words2:
        word = word.lower()
        print(word)
        if k2 == 10:
            break
        if word in ultraslovar:
            part_of_massiv2.append(ultraslovar.index(word))
            k2 += 1
    if k2 < 10:
        part_of_massiv2.extend([11501] * (10 - len(part_of_massiv2)))
    massiv2.append(part_of_massiv2)