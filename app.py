from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)

# Load the model and encoders
def load_model_and_encoders():
    try:
        with open('model/xgb_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('model/gender_encoder.pkl', 'rb') as f:
            gender_encoder = pickle.load(f)
        with open('model/smoking_encoder.pkl', 'rb') as f:
            smoking_encoder = pickle.load(f)
        return model, gender_encoder, smoking_encoder
    except Exception as e:
        print(f"Error loading model or encoders: {str(e)}")
        return None, None, None

# Load the model and encoders
model, gender_encoder, smoking_encoder = load_model_and_encoders()

# Define the feature names and their expected types
FEATURE_NAMES = [
    'gender',
    'age',
    'hypertension',
    'heart_disease',
    'smoking_history',
    'bmi',
    'HbA1c_level',
    'blood_glucose_level'
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None or gender_encoder is None or smoking_encoder is None:
            return jsonify({'error': 'Model or encoders not loaded properly'}), 500

        # Get values from the form
        gender = request.form['gender']
        smoking_history = request.form['smoking_history']
        
        # Encode categorical variables
        gender_encoded = gender_encoder.transform([gender])[0]
        smoking_encoded = smoking_encoder.transform([smoking_history])[0]
        
        # Create features dictionary
        features = {
            'gender': gender_encoded,
            'age': float(request.form['age']),
            'hypertension': int(request.form['hypertension']),
            'heart_disease': int(request.form['heart_disease']),
            'smoking_history': smoking_encoded,
            'bmi': float(request.form['bmi']),
            'HbA1c_level': float(request.form['HbA1c_level']),
            'blood_glucose_level': float(request.form['blood_glucose_level'])
        }
        
        # Create a DataFrame with the input features
        input_data = pd.DataFrame([features])
        
        # Ensure the columns are in the correct order
        input_data = input_data[FEATURE_NAMES]
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]
        
        result = {
            'prediction': int(prediction),
            'probability': round(float(probability) * 100, 2)
        }
        return jsonify(result)
        
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True) 