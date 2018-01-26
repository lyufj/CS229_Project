f = open('meta.txt', 'r')
data = f.read()
data = filter(None, data.split("\n"))
f.close()

num_category = 2

with open("meta_single_new.csv", "w") as outfile:
    for line in data:
        try:
            splat = filter(None, line.split("\t"))
            title = splat[1]
            title = title.replace(",", "")

            labels = splat[2].rstrip().split('|')
            labels = filter(None, labels)
            label = labels[num_category].split('[')
            sublable = label[0].replace(",", "")
            outfile.write(str(sublable) + "," + str(title) + "\n")

        except:
            pass