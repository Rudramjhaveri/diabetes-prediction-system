import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import pickle

# Read the dataset
df = pd.read_csv("diabetes_prediction_dataset.csv")

# Prepare the data
le_gender = LabelEncoder()
le_smoking = LabelEncoder()

# Fit and transform categorical variables
df['gender'] = le_gender.fit_transform(df['gender'])
df['smoking_history'] = le_smoking.fit_transform(df['smoking_history'])

# Split features and target
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model with the same parameters as in the notebook
model = XGBClassifier(
    objective='binary:logistic',
    random_state=42,
    use_label_encoder=False,
    eval_metric='logloss'
)

# Train the model
model.fit(X_train, y_train)

# Create model directory if it doesn't exist
import os
os.makedirs('model', exist_ok=True)

# Save the model and encoders
with open('model/xgb_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/gender_encoder.pkl', 'wb') as f:
    pickle.dump(le_gender, f)

with open('model/smoking_encoder.pkl', 'wb') as f:
    pickle.dump(le_smoking, f)

print("Model and encoders saved successfully!")

# Print model accuracy
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)
print(f"\nModel Performance:")
print(f"Training Accuracy: {train_accuracy:.4f}")
print(f"Testing Accuracy: {test_accuracy:.4f}") 