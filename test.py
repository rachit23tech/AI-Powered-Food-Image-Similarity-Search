import os
from search.find import search

files = os.listdir("dataset_flat")
image = files[0]

path = os.path.join("dataset_flat", image)
print(search(path))
