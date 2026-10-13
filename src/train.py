import os
import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def run_training():
    # 1. Load dataset (California Housing: 20,640 districts, 8 features)
    data = fetch_california_housing()
    X = data.data
    y = data.target  # median house value, in units of $100,000

    # 2. Train / test split (for sanity)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Train a model
    model = HistGradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)

    # 4. Quick eval just so we know it learned
    y_pred = model.predict(X_test)
    print(f"R2: {r2_score(y_test, y_pred):.3f}")
    print(f"Mean absolute error: ${mean_absolute_error(y_test, y_pred) * 100000:,.0f}")

    # 5. Make sure model/ directory exists
    os.makedirs("model", exist_ok=True)

    # 6. Save model to model/model.pkl
    joblib.dump(model, "model/model.pkl")
    print("Saved trained model to model/model.pkl")

if __name__ == "__main__":
    run_training()
