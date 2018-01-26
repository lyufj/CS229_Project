f = open('amazon-meta.txt', 'r')
data = f.read()
splat = data.split("\n\r")

link_meta = open('link_meta.txt','w')

ASIN = {}
link_list = {}
link_lib = {}

for paragraph in splat:
    paragraph = paragraph.splitlines()
    for i in xrange(paragraph.__len__()):
        line = paragraph[i].split(":", 1)
        line = [x.strip() for x in line]
        if line[0] == "Id":
            Id = line[1]
        if line[0] == "ASIN":
            ASIN[Id] = line[1]
        if line[0] == "similar":
            links = filter(None, line[1].split(' '))
            link_list[Id] = links

for item in ASIN:
    try:
        link = link_list[item]
        for num in xrange(int(link[0])):
            try:
                target = ASIN.keys()[ASIN.values().index(link[num + 1])]
                link_meta.write(str(item) + "\t" + str(target) + "\n")
            except ValueError:
                pass
    except KeyError:
        pass

link_meta.close()