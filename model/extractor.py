import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input

# Load fine-tuned model
full_model = load_model("food_finetuned_model.h5")

# Remove last classification layer
embedding_model = tf.keras.Model(
    inputs=full_model.input,
    outputs=full_model.layers[-2].output
)

def get_embedding(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (224,224))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    emb = embedding_model.predict(img)[0]
    return emb / np.linalg.norm(emb)
