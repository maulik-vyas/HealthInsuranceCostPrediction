import logging
import os

from click.formatting import join_options
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

# Load the trained model
try:
    model = joblib.load('cost_predictor_model.pkl')
    app.logger.info("Model loaded successfully")
except Exception as e:
    app.logger.error(f"Failed to load model: {str(e)}")
    raise Exception(f"Model loading failed: {str(e)}")

# Mapping for sex
sex_mapping = {'male': 1, 'female': 0}

region_mapping = {
    'northeast': [1, 0, 0, 0],
    'northwest': [0, 1, 0, 0],
    'southeast': [0, 0, 1, 0],
    'southwest': [0, 0, 0, 1]
}

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f'Exception occured: {str(e)}')
    return jsonify({'error': str(e)}), 500


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        age = int(data['age'])
        sex = sex_mapping.get(data['sex'], 0)
        bmi = float(data['bmi'])
        children = int(data['children'])
        smoker = int(data['smoker'])
        region = data['region']
        region_encoded = region_mapping.get(region, [0, 0, 0, 0])

        features = np.array([[age, sex, bmi, children, smoker] + region_encoded])
        app.logger.debug(f'Features for prediction: {features.tolist()}')

        prediction = model.predict(features)[0]
        app.logger.debug(f'Prediction: {prediction}')

        return jsonify({'predicted_cost': round(prediction, 2)})
    except Exception as e:
        app.logger.error(f'Prediction error: {str(e)}')
        raise e

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)