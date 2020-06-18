"""
searching
"""

from annoy import AnnoyIndex
import random


length_of_vector = 40
new_annoy_index = AnnoyIndex(length_of_vector, 'dot')
new_annoy_index.load('test.annoy')

n = 100
idx = 0
print(new_annoy_index.get_nns_by_item(idx, n))

vector = [random.gauss(0, 1) for _ in range(length_of_vector)]
print(new_annoy_index.get_nns_by_vector(vector, n))
