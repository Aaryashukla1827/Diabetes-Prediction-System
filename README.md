# 🩺 Diabetes Prediction System

A Machine Learning web application that predicts the likelihood of diabetes based on medical parameters.

## 🌐 Live Demo
https://diabetes-prediction-system-gegs7xgrruehxqvfg2mho6.streamlit.app/

## 🚀 Features

- 🔍 Real-time diabetes prediction
- 📊 Probability-based risk analysis
- 🎯 Risk categorization (Low / Medium / High)
- 🎨 Clean and interactive UI using Streamlit
- ✅ Input validation with realistic constraints


## 🧠 Model Details

- Algorithm: Logistic Regression
- Dataset: PIMA Indians Diabetes Dataset
- Features used:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age


## 🛠️ Tech Stack

- Python
- Scikit-learn
- Streamlit
- NumPy
- Pandas


## 📂 Project Structure
DiabetesPrediction/ 
├── app.py 
├── train_model.py 
├── model.pkl 
├── diabetes.csv 
├── requirements.txt 
└── README.md 

## ▶️ How to Run

```bash
git clone https://github.com/Aaryashukla1827/Diabetes-Prediction-System.git
cd Diabetes-Prediction-System

python3.11 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py

## 📊 Sample Output

### 🧾 Input Interface
![Input UI](screenshots/input.png)

### 📊 Prediction Result
![Result UI](screenshots/result.png)
