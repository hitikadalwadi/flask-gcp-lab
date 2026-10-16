import numpy as np
import joblib
import os
from train import run_training

# Input fields, in the order the model was trained on
FEATURE_NAMES = [
    "med_inc", "house_age", "ave_rooms", "ave_bedrms",
    "population", "ave_occup", "latitude", "longitude"
]

# Load the trained model
model = joblib.load("model/model.pkl")

def predict_price(med_inc, house_age, ave_rooms, ave_bedrms,
                  population, ave_occup, latitude, longitude):
    """Returns the predicted median house value in US dollars."""
    input_data = np.array([[med_inc, house_age, ave_rooms, ave_bedrms,
                            population, ave_occup, latitude, longitude]])
    prediction = model.predict(input_data)
    return float(prediction[0]) * 100000  # model output is in $100,000s

if __name__ == "__main__":
    if os.path.exists("model/model.pkl"):
        print("Model loaded successfully")
    else:
        os.makedirs("model", exist_ok=True)
        run_training()
