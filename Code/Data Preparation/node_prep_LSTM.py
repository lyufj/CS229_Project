import gensim
import numpy as np
import heapq
import random
import json

f = open('meta.txt', 'r')
data = f.read()
data = filter(None, data.split("\n"))
f.close()

f = open('hidden_states_full.csv', 'r')
feature_list = f.read()
feature_list = feature_list.replace('\r\n', '')
feature_list = feature_list.replace('[', '')
feature_list = feature_list.replace(']', '')
feature_list = feature_list.replace(' ', ',')
feature_list = filter(None, feature_list.split('|'))
f.close()

f = open('labels_3rd_127.txt', 'r')
label_list = f.read()
label_list = label_list.split('\n')
f.close()

num_category = 2

with open("node_BL_feature.json", "w") as outfile:
    for line in data:
        label = [0] * label_list.__len__()
        try:
            splat = filter(None, line.split("\t"))
            Id = int(splat[0])

            current_feature = feature_list[Id]
            current_feature = filter(None, current_feature.split('"'))
            feature = map(float, filter(None, current_feature[1].split(',')))

            labels = splat[2].rstrip().split('|')
            labels = filter(None, labels)
            sublabel = labels[num_category].split('[')
            index = label_list.index(sublabel[0])
            label[index] = 1

            test = random.random() < 0.2
            val = random.random() < 0.2

            json.dump({"test": test, "id": Id, "feature": feature,
                       "val": val, "label": list(label)}, outfile)
            outfile.write('\n')

        except:
            pass