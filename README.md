Disease Outbreak Prediction System 🏥
This project is a Machine Learning-powered application that predicts the likelihood of three diseases: Diabetes, Heart Disease, and Parkinson's Disease. It helps users quickly assess health risks based on input parameters using pre-trained models. The application is built using Streamlit for an interactive web interface.

📋 Project Features
Predicts the risk of the following diseases:
Diabetes: Based on input features such as pregnancies, glucose levels, blood pressure, and BMI.
Heart Disease: Uses parameters like cholesterol, blood pressure, and chest pain type.
Parkinson's Disease: Based on voice-related parameters like frequency and amplitude variations.
User-friendly interface powered by Streamlit.
Easy navigation through different prediction sections.

🛠 Tech Stack
Programming Language: Python
Libraries:
streamlit for the user interface
pickle for loading machine learning models
streamlit_option_menu for sidebar navigation
🚀 How to Run the Project
1️⃣ Clone the Repository

git clone <repository-url>
cd Disease-Outbreak-Prediction
2️⃣ Install Dependencies
Make sure you have Python 3.8 or above installed. Then run:
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run app.py
4️⃣ Access the App
The application will open in your default web browser at http://localhost:8501.

🧪 Example Inputs for Disease Prediction
Disease	Required Inputs
Diabetes	Pregnancies, Glucose Level, Blood Pressure, Skin Thickness, Insulin, BMI, Pedigree, Age
Heart Disease	Age, Gender, Chest Pain Type, Cholesterol, Blood Sugar, Max Heart Rate, etc.
Parkinson's	Frequency, Jitter, Shimmer, Harmonics, Spread, PPE, etc.
📂 Directory Structure

├── training_models/   # Saved ML models for prediction  
├── app.py             # Streamlit application code  
└── README.md           # Project documentation  

⚠️ Disclaimer
This application is a learning project and should not be used as a substitute for professional medical advice. Always consult healthcare professionals for accurate medical assessments.
