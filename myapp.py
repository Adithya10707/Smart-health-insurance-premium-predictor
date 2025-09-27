import streamlit as st
import numpy as np
import joblib

# Load trained model
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("🩺 Smart Health Insurance Premium Predictor for Apex Insure")

# --- FORM for inputs ---
with st.form("insurance_form"):
    st.header("📝 Enter Customer Details")

    age = st.slider("Age", min_value=18, max_value=100, value=27, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    dependents = st.number_input("Number of Dependents", min_value=0, step=1)
    region = st.selectbox("Region", ["Northwest", "Northeast", "Southwest", "Southeast"])
    marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])
    smoking_status = st.selectbox("Smoking Status", ["No Smoking", "Occasional", "Regular"])
    bmi = st.selectbox("BMI Status", ["Normal", "Underweight", "Overweight", "Obesity"])
    income_lakhs = st.slider("Income (in Lakhs)", min_value=1, step=1)
    employment_type = st.selectbox("Employment Type", ["Salaried", "Self-employed", "Freelancer"])
    income_level = st.selectbox("Income Level", ["<10L", "10L-25L", "25L-40L", ">40L"])
    medical_history = st.selectbox("Medical History", [
        "No Disease",
        "Thyroid",
        "High blood pressure",
        "Diabetes",
        "Diabetes & Thyroid",
        "Diabetes & High blood pressure",
        "Heart disease",
        "Diabetes & Heart disease",
        "High blood pressure & Heart disease"
    ])
    insurance_plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])

    # Submit button
    submit = st.form_submit_button("🔍 Predict Premium")


if submit:
    # Manual encoding
    gender_flag = 0 if gender == "Male" else 1
    region_dict = {"Northwest": 0, "Southeast": 1, "Northeast": 2, "Southwest": 3}
    region_flag = region_dict[region]

    marital_flag = 0 if marital_status == "Unmarried" else 1
    smoking_dict = {"No Smoking": 0, "Occasional": 1, "Regular": 2}
    smoking_flag = smoking_dict[smoking_status]

    bmi_dict = {"Normal": 0, "Underweight": 1, "Overweight": 2, "Obesity": 3}
    bmi_flag = bmi_dict[bmi]

    employment_dict = {"Salaried": 0, "Self-employed": 1, "Freelancer": 2}
    employment_flag = employment_dict[employment_type]

    income_level_dict = {"<10L": 0, "10L-25L": 1, "25L-40L": 2, ">40L": 3}
    income_level_flag = income_level_dict[income_level]

    medical_dict = {
        "No Disease": 0,
        "Thyroid": 1,
        "High blood pressure": 2,
        "Diabetes": 3,
        "Diabetes & Thyroid": 4,
        "Diabetes & High blood pressure": 5,
        "Heart disease": 6,
        "Diabetes & Heart disease": 7,
        "High blood pressure & Heart disease": 8
    }
    medical_flag = medical_dict[medical_history]

    plan_dict = {"Bronze": 0, "Silver": 1, "Gold": 2}
    plan_flag = plan_dict[insurance_plan]

    # Build feature array
    features = np.array([[age, gender_flag, dependents, region_flag, marital_flag,
                          smoking_flag, bmi_flag, employment_flag,income_lakhs, income_level_flag,
                          medical_flag, plan_flag]])

    # Make prediction
    prediction = model.predict(features)

    st.success(f"💰 Estimated Insurance Premium: ₹ {prediction[0]:,.2f}")


