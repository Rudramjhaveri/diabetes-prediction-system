# Diabetes_prediction
# Project Overview
This project focuses on building a predictive model for diagnosing diabetes using various machine-learning techniques. The dataset used contains patient information, including key health metrics. Based on these features, the objective is to identify whether a patient is diabetic or non-diabetic.

![diagram](https://github.com/user-attachments/assets/d832a203-f6b4-4f7c-ae60-e34970903948)

# Introduction
Diabetes is a chronic health condition where the body cannot regulate blood sugar levels effectively. Early detection of diabetes is crucial to prevent complications. This project employs machine learning models to predict diabetes based on patient health data.
# Dataset
The dataset used in this project includes the following features:
- Age: Numeric
- BMI: Numeric
- Blood Glucose Level: Numeric
- HbA1c Level: Numeric
- Gender: Categorical
- Heart Disease: Binary 
- Hypertension: Binary
- Smoking History: Categorical
- The target variable is: Diabetes: Binary (Diabetic/Non-diabetic)
# Data Preprocessing
- Missing Values: Handled by filling with appropriate statistics (mean/median).
- Encoding: Categorical features like Gender and Smoking History were encoded into numerical format.
- Scaling: StandardScaler was used to normalize numerical features (Age, BMI, HbA1c Level, and Blood Glucose Level).
# Handling Class Imbalance
The dataset was highly imbalanced, with a higher proportion of non-diabetic cases. To address this issue, a hybrid sampling approach was applied:
- SMOTE (Synthetic Minority Over-sampling Technique): Used to generate synthetic samples for the minority class (diabetic cases).
- Under-sampling: Applied to reduce the majority class (non-diabetic cases), balancing the dataset.
- This approach improved model performance and reduced bias towards the majority class.
# Modeling
The following machine-learning models were explored:
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- XGBoost Classifier
These models were evaluated using metrics like accuracy, precision, recall, and F1-score.
# Evaluation
The XGBoost Classifier performed the best, achieving:
Accuracy: 95%
Precision: 95%
Recall: 95%
F1-Score:95%
The confusion matrix showed a high true positive rate for diabetic predictions, enhanced by handling the class imbalance effectively.
# Feature Importance
The feature importance plot from the XGBoost model highlighted the most influential features:
- HbA1c Level: Most important predictor.
- Blood Glucose Level: Second most significant predictor.
- Age and BMI also contributed significantly.
# Conclusion
The XGBoost model provided the best results for predicting diabetes, with high accuracy and recall. Handling class imbalance with SMOTE and under-sampling improved model performance. The key features identified, including HbA1c Level and Blood Glucose Level, are essential indicators of diabetes risk.
# Technologies used
- Jupyter Notebook
- Python
- Python libraries
  1) Pandas
  2) Numpy
  3) Seaborn
  4) Scikit-learn
  5) Matplotlib
# Model Deployment Using Streamlit
https://diabetesprediction-fqzmsmfvvuclzyjvygtsou.streamlit.app/
