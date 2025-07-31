from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flask_cors import cross_origin

app = Flask(__name__)


models = {
    "opsti": {
        "model": joblib.load('modeli/JB/rf_scaler_prev_weight.joblib'),
        "preprocess": joblib.load('modeli/JB/preprocess_pipeline.joblib')
    },
    "gradiska": {
        "model": joblib.load('modeli/JB/gradiska_scaler_prev_weight.joblib'),
        "preprocess": joblib.load('modeli/JB/preprocess_pipeline_gradiska.joblib')
    }
}

@app.route('/predict_weight', methods=['POST'])
@cross_origin()
def predict_weight():
    try:
        data = request.get_json()

        
        if "model" not in data or data["model"] not in models:
            return jsonify({'error': 'Missing or invalid model type. Use "opsti" or "gradiska".'}), 400

        required_keys = ['AvgPixelCount', 'NumberOfDaysFromStart', 'PreviousWeight']
        if not all(key in data for key in required_keys):
            return jsonify({'error': 'Missing required keys in request data'}), 400

        
        selected_model = models[data["model"]]["model"]
        selected_preprocess = models[data["model"]]["preprocess"]

        
        input_df = pd.DataFrame([data], columns=required_keys)
        transformed_features = selected_preprocess.transform(input_df)

        
        result = selected_model.predict(transformed_features)

        return jsonify({'predicted_weight': result[0]}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Test ok!"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
