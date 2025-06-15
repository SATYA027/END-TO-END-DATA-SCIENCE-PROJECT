
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample dataset
data = {
    "review": [
        "This movie was amazing and thrilling!",
        "Worst film ever. Don't waste your time.",
        "A beautiful story with great acting.",
        "Terrible plot. Very boring.",
        "Loved the characters and emotion.",
        "Disgusting and poorly directed."
    ],
    "label": [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

# Vectorize and train
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["review"])
y = df["label"]
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
