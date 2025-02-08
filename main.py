import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os

# Page Configuration
st.set_page_config(
    page_title="Disease Outbreak Prediction System",
    layout="wide",
    page_icon="🏥"
)

# Disclaimer
st.warning("⚠️ This is just a prediction model. Consult a doctor for accurate diagnosis.")

# Load Machine Learning Models
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/trained_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/trained_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/trained_models/parkinson_model.sav', 'rb'))

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Disease Prediction System",
        options=["Diabetes Prediction", "Heart Disease Prediction", "Parkinson’s Prediction"],
        icons=["activity", "heart", "person"],
        menu_icon="hospital-fill",
        default_index=0
    )

def check_inputs(inputs):
    if any(x == "" or x is None for x in inputs):
        st.warning("⚠️ Please fill in all fields before proceeding.")
        return False
    return True

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using Machine Learning")
    st.write("Please enter the following details to predict diabetes risk.")

    pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1)
    glucose_level = st.number_input("Glucose Level (mg/dL)", min_value=0.1)
    blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=0.1)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0.1)
    insulin = st.number_input("Insulin Level (IU/mL)", min_value=0.1)
    bmi = st.number_input("BMI Value", min_value=0.1)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function Value", min_value=0.1)
    age = st.number_input("Age of the Person", min_value=1, step=1)

    if st.button("Predict Diabetes Risk"):
        user_input = [pregnancies, glucose_level, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]
        if check_inputs(user_input):
            prediction = diabetes_model.predict([user_input])
            st.success("This person is not diabetic.") if prediction[0] == 0 else st.error("This person is diabetic.")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using Machine Learning")
    st.write("Please enter the following details to predict heart disease risk.")
    
    age = st.number_input("Age of the Person", min_value=1, step=1)
    sex = st.selectbox("Gender", ["Male", "Female"])
    cp = st.number_input("Chest Pain Type (1-4)", min_value=1, max_value=4, step=1)
    trestbps = st.number_input("Resting Blood Pressure (mmHg)", min_value=0.1)
    chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0.1)
    fbs = st.number_input("Fasting Blood Sugar (mg/dL)", min_value=0.1)
    restecg = st.number_input("Resting Electrocardiographic Results", min_value=0.1)
    max_heart_rate = st.number_input("Maximum Heart Rate Achieved", min_value=0.1)
    exang = st.number_input("Exercise Induced Angina (1 = Yes, 0 = No)", min_value=0, max_value=1, step=1)
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.1)
    slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0.1)
    thal = st.number_input("Thalassemia (0-3)", min_value=0.0, max_value=4.0)
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, step=1)
    
    if st.button("Predict Heart Disease Risk"):
        gender = 1 if sex == "Male" else 0
        user_input = [age, gender, cp, trestbps, chol, fbs, restecg, max_heart_rate, exang, oldpeak, slope, thal, ca]
        if check_inputs(user_input):
            prediction = heart_disease_model.predict([user_input])
            st.success("This person does not have heart disease.") if prediction[0] == 0 else st.error("This person has heart disease.")

# Parkinson’s Disease Prediction Page
if selected == "Parkinson’s Prediction":
    st.title("Parkinson’s Disease Prediction using Machine Learning")
    st.write("Please enter the following details to predict Parkinson’s disease risk.")
    
    inputs = [
        st.number_input("Fundamental Frequency (Fo) in Hz", min_value=0.1),
        st.number_input("Highest Fundamental Frequency (Fhi) in Hz", min_value=0.1),
        st.number_input("Lowest Fundamental Frequency (Flo) in Hz", min_value=0.1),
        st.number_input("Jitter Percentage (%)", min_value=0.1),
        st.number_input("Absolute Jitter", min_value=0.1),
        st.number_input("Relative Amplitude Perturbation (RAP)", min_value=0.1),
        st.number_input("Pitch Period Perturbation Quotient (PPQ)", min_value=0.1),
        st.number_input("DDP Jitter", min_value=0.1),
        st.number_input("Shimmer", min_value=0.1),
        st.number_input("Shimmer in dB", min_value=0.1),
        st.number_input("Amplitude Perturbation Quotient (APQ3)", min_value=0.1),
        st.number_input("Amplitude Perturbation Quotient (APQ5)", min_value=0.1),
        st.number_input("MDVP APQ", min_value=0.1),
        st.number_input("Shimmer DDA", min_value=0.1),
        st.number_input("Noise-to-Harmonics Ratio (NHR)", min_value=0.1),
        st.number_input("Harmonics-to-Noise Ratio (HNR)", min_value=0.1),
        st.number_input("Recurrence Period Density Entropy (RPDE)", min_value=0.1),
        st.number_input("Detrended Fluctuation Analysis (DFA)", min_value=0.1),
        st.number_input("Spread 1", min_value=0.1),
        st.number_input("Spread 2", min_value=0.1),
        st.number_input("D2", min_value=0.1),
        st.number_input("Pitch Period Entropy (PPE)", min_value=0.1)
    ]
    
    if st.button("Predict Parkinson’s Disease Risk") and check_inputs(inputs):
        prediction = parkinsons_model.predict([inputs])
        st.success("This person does not have Parkinson’s disease.") if prediction[0] == 0 else st.error("This person has Parkinson’s disease.")
