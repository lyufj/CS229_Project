f = open('amazon-meta.txt', 'r')
data = f.read()

titles = open('titles.txt','w')
meta = open('meta.txt','w')

splat = data.split("\n\r")
category = {}

for paragraph in splat:
    paragraph = paragraph.splitlines()
    for i in xrange(paragraph.__sizeof__()):
        try:
            line = paragraph[i].split(":", 1)
            line = [x.strip() for x in line]
            if line[0] == "Id":
                Id = line[1]
            if line[0] == "title":
                title = line[1].rstrip().split(" ")
                titles.write(line[1] + "\n")
            if line[0] == "categories":
                categories = int(line[1])
                current_category = {paragraph[i + 1 + num].strip() for num in xrange(categories)}
                category.update(current_category)
        except:
            pass
    try:
        meta.write(str(Id) + "\t" + str(title) + "\t" + str(",".join(current_category)) + "\n" )
    except:
        pass

titles.close()
meta.close()