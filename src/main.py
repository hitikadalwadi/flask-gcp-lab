from flask import Flask, request, jsonify
from predict import predict_price, FEATURE_NAMES
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(silent=True) or {}

    missing = [name for name in FEATURE_NAMES if name not in data]
    if missing:
        return jsonify({'error': f'missing fields: {missing}'}), 400
    try:
        values = {name: float(data[name]) for name in FEATURE_NAMES}
    except (TypeError, ValueError):
        return jsonify({'error': 'all fields must be numeric'}), 400

    price = predict_price(**values)
    return jsonify({'prediction': round(price, 2)})

if __name__ == '__main__':
    app.run(
        debug=False, #changed because it can leak into prod
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080))
    )
