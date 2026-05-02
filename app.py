import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Diabetes Prediction")

# CSS
st.markdown("""...""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🩺 Diabetes Prediction System")
st.markdown("Enter valid medical details below")

# 🔥 Container starts
with st.container():
    st.subheader("📋 Enter Patient Details")

    # 🔥 COLUMNS HERE
    col1, col2 = st.columns(2)

    # LEFT SIDE
    with col1:
        preg = st.number_input("Pregnancies", min_value=0)
        glucose = st.number_input("Glucose", min_value=0)
        skin = st.number_input("Skin Thickness", min_value=0)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)


    # RIGHT SIDE
    with col2:
        bp = st.number_input("Blood Pressure", min_value=0)
        insulin = st.number_input("Insulin", min_value=0)
        bmi = st.number_input("BMI", min_value=0.0)
        age = st.number_input("Age", min_value=1)

# Button outside container (clean UI)
if st.button("🔍 Predict", use_container_width=True):
    input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    # Prediction
    prediction = model.predict(input_data)

    # 🔥 ADD THIS HERE
    prob = model.predict_proba(input_data)
    risk = prob[0][1]

    # Result
    if prediction[0] == 0:
        st.success("✅ Not Diabetic")
    else:
        st.error("⚠️ Diabetic")

    # 🔥 SHOW PROBABILITY (THIS LINE)
    st.metric("Diabetes Risk", f"{prob[0][1]*100:.2f}%")
    if risk < 0.3:
        st.success("🟢 Low Risk")
    elif risk < 0.7:
        st.warning("🟡 Medium Risk")
    else:
        st.error("🔴 High Risk")
