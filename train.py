# train.py
from sklearn.linear_model import LinearRegression
import joblib

X = [[1], [2], [3], [4]]
y = [100, 200, 300, 400]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")