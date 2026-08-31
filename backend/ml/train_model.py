import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.abspath(
    os.path.join(BASE_DIR, "..", "data", "robot_sensor_data.csv")
)

print(csv_path)
data = pd.read_csv(csv_path)
print(csv_path)
print(os.path.exists(csv_path))


X = data[["temperature", "vibration"]]
y = data["status"]

model = DecisionTreeClassifier()
model.fit(X, y)

model_path = os.path.join(BASE_DIR, "model.pkl")
joblib.dump(model, model_path)

print("✅ Model trained successfully!")
print("✅ model.pkl created successfully!")
