import streamlit as st
import pandas as pd
import pickle

# 🎯 Load model and encoders
model = pickle.load(open('svm_lineae_model.pkl', 'rb'))
status_encoder = pickle.load(open('Attribute1.pkl', 'rb'))
credit_history_encoder = pickle.load(open('Attribute3.pkl', 'rb'))
purpose_encoder = pickle.load(open('Attribute4.pkl', 'rb'))
savings_encoder = pickle.load(open('Attribute6.pkl', 'rb'))
employment_encoder = pickle.load(open('Attribute7.pkl', 'rb'))
personal_status_encoder = pickle.load(open('Attribute9.pkl', 'rb'))
other_debtors_encoder = pickle.load(open('Attribute10.pkl', 'rb'))
property_encoder = pickle.load(open('Attribute12.pkl', 'rb'))
other_installments_encoder = pickle.load(open('Attribute14.pkl', 'rb'))
housing_encoder = pickle.load(open('Attribute15.pkl', 'rb'))
job_encoder = pickle.load(open('Attribute17.pkl', 'rb'))
telephone_encoder = pickle.load(open('Attribute19.pkl', 'rb'))
foreign_worker_encoder = pickle.load(open('Attribute20.pkl', 'rb'))

# Streamlit UI
st.title(" German Credit Risk Prediction")
st.markdown("Enter applicant details to predict credit risk:")

#  Numerical Inputs
duration = st.number_input("Duration (in months)", min_value=0)
credit_amount = st.number_input("Credit Amount", min_value=0)
installment_rate = st.number_input("Installment Rate (%)", min_value=1, max_value=4)
residence_since = st.number_input("Years at Current Residence", min_value=0)
age = st.number_input("Age", min_value=18)
existing_credits = st.number_input("Number of Existing Credits", min_value=0)
liable_people = st.number_input("Number of Liable People", min_value=1, max_value=2)

# Categorical Inputs
status = st.selectbox("Status", status_encoder.classes_)
credit_history = st.selectbox("Credit History", credit_history_encoder.classes_)
purpose = st.selectbox("Purpose", purpose_encoder.classes_)
savings = st.selectbox("Savings Account", savings_encoder.classes_)
employment = st.selectbox("Employment Duration", employment_encoder.classes_)
personal_status = st.selectbox("Personal Status", personal_status_encoder.classes_)
other_debtors = st.selectbox("Other Debtors", other_debtors_encoder.classes_)
property = st.selectbox("Property", property_encoder.classes_)
other_installments = st.selectbox("Other Installments", other_installments_encoder.classes_)
housing = st.selectbox("Housing", housing_encoder.classes_)
job = st.selectbox("Job", job_encoder.classes_)
telephone = st.selectbox("Telephone", telephone_encoder.classes_)
foreign_worker = st.selectbox("Foreign Worker", foreign_worker_encoder.classes_)

# Encode categorical features
status_encoded = status_encoder.transform([status])[0]
credit_history_encoded = credit_history_encoder.transform([credit_history])[0]
purpose_encoded = purpose_encoder.transform([purpose])[0]
savings_encoded = savings_encoder.transform([savings])[0]
employment_encoded = employment_encoder.transform([employment])[0]
personal_status_encoded = personal_status_encoder.transform([personal_status])[0]
other_debtors_encoded = other_debtors_encoder.transform([other_debtors])[0]
property_encoded = property_encoder.transform([property])[0]
other_installments_encoded = other_installments_encoder.transform([other_installments])[0]
housing_encoded = housing_encoder.transform([housing])[0]
job_encoded = job_encoder.transform([job])[0]
telephone_encoded = telephone_encoder.transform([telephone])[0]
foreign_worker_encoded = foreign_worker_encoder.transform([foreign_worker])[0]

# Create input DataFrame
input_data = pd.DataFrame({
    'Duration': [duration],
    'Credit Amount': [credit_amount],
    'Installment Rate': [installment_rate],
    'Residence Since': [residence_since],
    'Age': [age],
    'Existing Credits': [existing_credits],
    'Liable People': [liable_people],
    'Status': [status_encoded],
    'Credit History': [credit_history_encoded],
    'Purpose': [purpose_encoded],
    'Savings': [savings_encoded],
    'Employment': [employment_encoded],
    'Personal Status': [personal_status_encoded],
    'Other Debtors': [other_debtors_encoded],
    'Property': [property_encoded],
    'Other Installments': [other_installments_encoded],
    'Housing': [housing_encoded],
    'Job': [job_encoded],
    'Telephone': [telephone_encoded],
    'Foreign Worker': [foreign_worker_encoded]
})

# Predict
if st.button("Predict Credit Risk"):
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("✅ Good Credit Risk")
    else:
        st.error("⚠ Bad Credit Risk")