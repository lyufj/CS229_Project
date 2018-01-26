import json

f = open('meta.txt', 'r')
data = f.read()
data = filter(None, data.split("\n"))
f.close()

f = open('labels_3rd_127.txt', 'r')
label_list = f.read()
label_list = label_list.split('\n')
f.close()

num_category = 2

class_map = dict()
for line in data:
    label = [0] * label_list.__len__()
    try:
        splat = filter(None, line.split("\t"))
        Id = splat[0]

        labels = splat[2].rstrip().split('|')
        labels = filter(None, labels)
        sublabel = labels[num_category].split('[')
        index = label_list.index(sublabel[0])
        label[index] = 1

        class_map.update({Id: list(label)})

    except:
        pass

with open("amazon0302-class_map.json", "w") as outfile:
    json.dump(class_map, outfile)