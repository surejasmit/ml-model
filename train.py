# train.py
from sklearn.linear_model import LinearRegression
import joblib

# Training data (2 features)
X = [
    [1, 10],
    [2, 20],
    [3, 30],
    [4, 40]
]

y = [100, 200, 300, 400]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")