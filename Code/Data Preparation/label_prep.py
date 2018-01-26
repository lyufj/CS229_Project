f = open('meta.txt', 'r')
data = f.read()

num_category = 3

all_labels = open('labels_3.txt','w')

label_set = set()

IndexErr = 0

for line in filter(None, data.split("\n")):
    try:
        splat = filter(None, line.split("\t"))
        Id = splat[0]
        title = splat[1]
        labels = splat[2].rstrip().split('||')
        for label in labels:
            sublabels = filter(None, label.split('|'))
            for i, sublable in enumerate(sublabels):
                sub = sublable.rstrip().split('[')
                sublabels[i] = sub[0]
            sublabels = filter(None, sublabels)
            label_set.update(sublabels[0:num_category])
    except IndexError:
        IndexErr += 1
        pass

for lab in sorted(label_set):
    all_labels.write(lab + "\n")

print IndexErr

all_labels.close()