import os
import json

print('Love me some JSON')
path = os.getcwd()
path = os.path.join(path, "comments")
files = os.listdir(path)

total_data = {}
i = 0
for f in files:
    if f == ".DS_Store":
        continue
    file_path = os.path.join(path, f)
    with open(file_path, 'r') as data:
        json_data = json.load(data)
        for k in json_data.keys():
            review = {}
            review['score'] = json_data[k]['score']
            review['comment'] = json_data[k]['comment']
            total_data[i] = review
            print(i)
            i += 1

outfile = os.path.join(os.getcwd(), "rmp_data.json")
with open(outfile, 'w') as out:
    json.dump(total_data, out, indent=True)
