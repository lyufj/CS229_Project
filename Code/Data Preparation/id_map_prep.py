import json

id_map = dict()
for Id in range(1, 548552):
    id_map.update({Id: Id})

with open("amazon0302-id_map.json", "w") as outfile:
    json.dump(id_map, outfile)

# with open("amazon0302-class_map.json") as infile:
#     data = json.load(infile)
#
# id_map = dict()
# for Id in data:
#     id_map.update({Id: Id})
#
# with open("amazon0302-id_map.json", "w") as outfile:
#     json.dump(id_map, outfile)