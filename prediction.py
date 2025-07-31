from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import cross_origin

app = Flask(__name__)


model_rf = joblib.load('modeli/JB/rf_scaler_prev_weight.joblib')
preprocess = joblib.load('modeli/JB/preprocess_pipeline.joblib')

@app.route('/predict_weight', methods=['POST'])
@cross_origin()
def predict_weight():
    try:
        data = request.get_json()

        required_keys = ['AvgPixelCount', 'NumberOfDaysFromStart', 'PreviousWeight']
        if not all(key in data for key in required_keys):
            return jsonify({'error': 'Missing required keys in request data'}), 400

        input_df = pd.DataFrame([data], columns=required_keys)

       
        transformed_features = preprocess.transform(input_df)

        result = model_rf.predict(transformed_features)

        return jsonify({'predicted_weight': result[0]}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run()
