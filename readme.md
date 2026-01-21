# 🍕 AI-Powered Food Image Similarity Search

A deep learning-based image similarity system that retrieves visually similar food images using CNN embeddings and cosine similarity.

---

## 🚀 Features
- Fine-tuned ResNet50 for food image embeddings
- Embedding-based similarity search (not classification)
- Real-time image upload and search
- Streamlit web dashboard
- Scalable architecture for large datasets
- Ready for FAISS integration

---

## 🧠 How it Works
1. Image is passed through fine-tuned ResNet50
2. Embeddings are extracted
3. Cosine similarity is computed
4. Top-k similar images are retrieved
5. Results shown in web UI

---

## 🖼 Demo
![demo](demo.png)

---

## ⚙️ Installation

```bash
git clone https://github.com/rachit23tech/food-image-similarity.git
cd food-image-similarity
pip install -r requirements.txt
