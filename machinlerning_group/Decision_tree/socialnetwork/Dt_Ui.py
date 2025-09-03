import streamlit as st
import numpy as np
import pickle


#load model 

with open("dt_model.pkl","rb") as file:
    model=pickle.load(file)

with open ("Gender_enc.pkl","rb") as f:
    Gender_en=pickle.load(f)

#title

st.title("Social Network_ads")

Gender_in=list(Gender_en.classes_)


Gender=st.selectbox("passenger sex ",Gender_in)
Age=st.slider("Age",min_value=18,max_value=80,)
EstimatedSalary=st.number_input('Salary',min_value=15000,)

Gender_encod = Gender_en.transform([Gender])[0]

if st.button("Predict"):
    input_data=np.array([[Gender_encod,Age,EstimatedSalary]])
    prediction=model.predict(input_data)[0]

    if prediction==1:
        st.success("prediction: Will Purchase")
    else:
        st.error("pridiction: will not purchase")