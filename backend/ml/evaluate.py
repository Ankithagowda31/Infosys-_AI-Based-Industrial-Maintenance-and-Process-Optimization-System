import joblib


def evaluate():
    model = joblib.load("model.pkl")
    print("Model loaded successfully.")
    print("Model is ready for prediction.")


if __name__ == "__main__":
    evaluate()
