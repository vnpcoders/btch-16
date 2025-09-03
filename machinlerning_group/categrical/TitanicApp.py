import streamlit as st
import numpy as np
import pickle


with open("log_model.pkl","rb")as f:
    model= pickle.load(f)

with open("sex_encoder.pkl","rb") as f:
    sex_enc= pickle.load(f)

with open("emb_encoder.pkl","rb") as f:
    emb_enc= pickle.load(f)

st.title("Titanic Survival Prediction App")

sex_options=list(sex_enc.classes_)
emb_options=list(emb_enc.classes_)
psngr_class=[1,2,3]

#user inputs

pclass=st.selectbox("passenger class",psngr_class)
sex=st.selectbox("passenger sex ",sex_options)
Age=st.slider("passenger Age",min_value=0,max_value=80,)
SibSp=st.slider('SibSp',min_value=0,max_value=8)
parch=st.slider('parch',min_value=0,max_value=6)
Fare=st.number_input(" Farevpaid",min_value=0)
Embarked=st.selectbox("Embarked",emb_options)

sex_encoder = sex_enc.transform([sex])[0]
emb_encoder = emb_enc.transform([Embarked])[0]



if st.button("Predict"):
    input_data=np.array([[pclass,sex_encoder,Age,SibSp,parch,Fare,emb_encoder]])
    prediction=model.predict(input_data)[0]