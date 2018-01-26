import json

link = []
with open("link_0302.json") as fo:
    for line in fo:
        link.append(json.loads(line))
node = []
with open("node_LSTM.json") as fo:
    for line in fo:
        node.append(json.loads(line))

with open("amazon0302_LSTM-G.json", "w") as outfile:
    json.dump({"directed": False, "graph": {"name": "disjoint_union( ,  )"}, "nodes": node, "links": link,
               "multigraph": False}, outfile)