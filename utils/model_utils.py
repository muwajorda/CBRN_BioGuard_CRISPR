import pickle
import os
import numpy as np

model_path = os.path.join(os.path.dirname(__file__), "..", "model", "model.pkl")
vectorizer_path = os.path.join(os.path.dirname(__file__), "..", "model", "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

def classify_sequence(seq):
    X = vectorizer.transform([seq])
    prediction = model.predict(X)[0]
    label = "Threat" if prediction == 1 else "Benign"
    return label, prediction

