import random
import json

f = open('amazon0302.txt', 'r')
data = f.read()
data = filter(None, data.split("\n"))
f.close()

with open("link_0302.json", "w") as outfile:
    for line in data:
        try:
            splat = filter(None, line.split("\t"))
            node1 = int(splat[0])

            node2 = int(splat[1])

            test_removed = random.random() < 0.2
            train_removed = random.random() < 0.8

            json.dump({"test_removed": test_removed, "train_removed": train_removed,
                       "target": node1, "source": node2}, outfile)
            outfile.write('\n')

        except:
            pass