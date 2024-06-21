import json, time

with open("SORTED.jsonl", "r") as f:
    x = list(f)
posts = len(x)

data = [[0] for i in range(posts)]
с = 0
for json_str in x:
    data[с] = (json.loads(json_str))
    с += 1
F = ""
for i in range(posts):
    start_time = time.time()
    for j in range(len(data[i])):
        F += (data[i][j]['text'])
    end_time = time.time()
with open("obuch.txt", "w+", encoding="utf-8") as my_file:
    my_file.write(F)
