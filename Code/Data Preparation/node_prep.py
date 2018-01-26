import gensim
import numpy as np
import heapq
import random
import json

model = gensim.models.Word2Vec.load("title_model")

f = open('meta.txt', 'r')
data = f.read()
data = filter(None, data.split("\n"))
f.close()

f = open('labels_3rd_127.txt', 'r')
label_list = f.read()
label_list = label_list.split('\n')
f.close()

num_category = 2

with open("node_BL.json", "w") as outfile:
    for line in data:
        label = [0] * label_list.__len__()
        try:
            splat = filter(None, line.split("\t"))
            Id = int(splat[0])

            title = splat[1].split()
            feature = np.array([sum(x) for x in zip(*model[title])])
            # threshold = heapq.nlargest(3, feature)
            # feature[feature < threshold[2]] = 0
            # feature[feature >= threshold[2]] = 1

            labels = splat[2].rstrip().split('|')
            labels = filter(None, labels)
            sublabel = labels[num_category].split('[')
            index = label_list.index(sublabel[0])
            label[index] = 1

            test = random.random() < 0.2
            val = random.random() < 0.2

            json.dump({"test": test, "id": Id, "feature": list(feature),
                       "val": val, "label": list(label)}, outfile)
            outfile.write('\n')

        except:
            pass