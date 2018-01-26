import gensim
import logging
import numpy as np

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

f = open('titles.txt', 'r')
data = f.read()
splat = data.split("\n")
sentences = []
for line in splat:
    sentences.append(line.rstrip().split(" "))

model = gensim.models.Word2Vec(sentences, size=20, window=5, min_count=1, workers=4)

model.save('title_model')