"""
indexing.py
"""


from annoy import AnnoyIndex
import random


length_of_vector = 40
annoy_index = AnnoyIndex(length_of_vector, 'dot')  
for idx in range(1000):
    vector = [random.gauss(0, 1) for _ in range(length_of_vector)]
    annoy_index.add_item(idx, vector)

annoy_index.build(10) 
annoy_index.save('test.annoy')
