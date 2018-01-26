import json
import numpy as np

# word2vec feature, size 20
# LSTM feature, size 300

feats = np.zeros(shape=(548552,300))

with open("node_GRU.json") as fo:
    for line in fo:
        data = json.loads(line)
        Id = int(data["id"])
        feature = np.array(data["feature"])
        feats[Id, :] = feature

np.save('GRU-feats.npy', feats)