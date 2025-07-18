# 🩺 Diabetes Prediction System

## 🔍 Project Overview
This project focuses on building a machine learning model to predict diabetes based on patient health data. Using a variety of ML techniques, the goal is to classify patients as diabetic or non-diabetic by analyzing key medical indicators.

---

## 🧠 Introduction
Diabetes is a chronic disease where the body struggles to manage blood sugar levels. Early detection is vital to prevent severe complications. This system leverages ML to identify diabetes risk using patient records, improving diagnostic accuracy and decision-making.

---

## 📊 Dataset Description
The dataset includes the following features:

- **Age** (Numeric)  
- **BMI** (Numeric)  
- **Blood Glucose Level** (Numeric)  
- **HbA1c Level** (Numeric)  
- **Gender** (Categorical)  
- **Heart Disease** (Binary)  
- **Hypertension** (Binary)  
- **Smoking History** (Categorical)  
- **Target Variable**: `Diabetes` (Binary: Diabetic/Non-diabetic)

---

## 🧹 Data Preprocessing

- **Missing Values**: Imputed using statistical methods (mean/median).
- **Encoding**: Categorical variables (e.g., Gender, Smoking History) were label-encoded.
- **Scaling**: Applied `StandardScaler` to normalize numeric features (e.g., Age, BMI, HbA1c, Glucose Level).

---

## ⚖️ Handling Class Imbalance

- **Problem**: More non-diabetic than diabetic cases.
- **Solution**: Applied a hybrid sampling strategy:
  - `SMOTE` to oversample minority class (diabetic).
  - Under-sampling to reduce the majority class (non-diabetic).
- ✅ Result: Balanced dataset with improved model performance and fairness.

---

## 🤖 Modeling

Explored the following ML algorithms:

- Logistic Regression  
- Support Vector Machine (SVM)  
- Decision Tree  
- XGBoost Classifier

📈 **Metrics Used**:
- Accuracy  
- Precision  
- Recall  
- F1-Score  

---

## ✅ Evaluation Results

🟢 **Best Model**: XGBoost Classifier  
- **Accuracy**: 95%  
- **Precision**: 95%  
- **Recall**: 95%  
- **F1-Score**: 95%

📊 The model showed excellent predictive power and balanced sensitivity and specificity.

---

## 📌 Feature Importance

Key predictors based on XGBoost importance:

1. **HbA1c Level** (Most important)
2. **Blood Glucose Level**
3. **Age**
4. **BMI**

---

## ✅ Conclusion

The XGBoost-based diabetes prediction system achieves high accuracy and reliability, especially after addressing class imbalance. The most influential indicators—**HbA1c** and **Glucose Level**—highlight the importance of medical data in predictive modeling.

---

## 🛠️ Technologies Used

- **Language**: Python  
- **Environment**: Jupyter Notebook  
- **Libraries**:
  - `Pandas`
  - `NumPy`
  - `Scikit-learn`
  - `Matplotlib`
  - `Seaborn`
  - `XGBoost`

---

## 🚀 Model Deployment

Deployed  


---

## 📂 Project Title
**Diabetes Prediction System**

---

