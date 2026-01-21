import numpy as np
from model.extractor import get_embedding

db = np.load("embeddings.npy")
names = np.load("names.npy", allow_pickle=True)

def search(image_path, top_k=5, return_scores=False):
    q = get_embedding(image_path)

    scores = np.dot(db, q)
    idx = np.argsort(scores)[::-1][:top_k]

    results = [names[i] for i in idx]
    sim_scores = [float(scores[i]) for i in idx]

    if return_scores:
        return results, sim_scores

    return results
