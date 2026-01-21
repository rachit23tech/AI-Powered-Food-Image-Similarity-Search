import os
import numpy as np
from model.extractor import get_embedding

embeddings = []
names = []

for img in os.listdir("dataset_flat"):
    if not img.lower().endswith((".jpg", ".png", ".jpeg")):
        continue

    path = os.path.join("dataset_flat", img)
    emb = get_embedding(path)

    embeddings.append(emb)
    names.append(img)

np.save("embeddings.npy", embeddings)
np.save("names.npy", names)

print("Embeddings saved!")
