import os
import random
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def random_dna(length=100):
    return ''.join(random.choices("ATCG", k=length))

# Simulate dataset
sequences = [random_dna() for _ in range(1000)]
labels = [random.randint(0, 1) for _ in range(1000)]

# Vectorize
vectorizer = CountVectorizer(analyzer='char', ngram_range=(3, 3))
X = vectorizer.fit_transform(sequences)

# Train model
model = MultinomialNB()
model.fit(X, labels)

# Save vectorizer and model
os.makedirs("model", exist_ok=True)
with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Mock model and vectorizer saved to /model/")

