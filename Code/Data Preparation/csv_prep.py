f = open('meta.txt', 'r')
data = f.read()
data = filter(None, data.split("\n"))
f.close()

with open("meta.csv", "w") as outfile:
    for line in data:
        try:
            splat = filter(None, line.split("\t"))
            title = splat[1]
            title.replace(",", "")

            labels = splat[2].rstrip().split('||')
            for sublabels in labels:
                sublabels = filter(None, sublabels.split('|'))
                for i in range(0,3):
                    outfile.write(str(sublabels[i]) + "," + str(title) + "\n")

        except:
            pass