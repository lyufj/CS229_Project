f = open('meta.txt', 'r')
data = f.read()

num_category = 2

all_labels = open('labels_3rd.txt','w')

label_set = set()

IndexErr = 0

for line in filter(None, data.split("\n")):
    try:
        splat = filter(None, line.split("\t"))
        Id = splat[0]
        title = splat[1]
        labels = splat[2].rstrip().split('|')
        labels = filter(None, labels)
        label = labels[num_category].split('[')
        label_set.update(label[0:1])
    except IndexError:
        IndexErr += 1
        pass

for lab in label_set:
    all_labels.write(lab + "\n")

print IndexErr

all_labels.close()