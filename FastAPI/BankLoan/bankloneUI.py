import numpy as np
import pickle
import streamlit as st

model=pickle.load(open("rf_model.pkl","rb"))

st.title("CHECK ELEGIBLITY FOR LOAN AMOUNT ")


Age=st.slider("Age",min_value=18,max_value=80,)
Experince=st.number_input("Experince",min_value=0,)
Income=st.number_input("Income",min_value=0,)
Family=st.number_input("Family",min_value=1,max_value=20)
CCAvg=st.number_input("CCAvg",min_value=0,)
Education=st.selectbox("Education",["😒undergraduat","😊graduat","😂postgraduat"])
Mortgage=st.number_input("Mortgage",min_value=0)
Securities_Account=st.selectbox("Securities_Account",["yes","No"])
CD_Account=st.selectbox("CD_Account",["yes","No"])
Online=st.selectbox("Online",["yes","No"])
CreditCard=st.selectbox("CreditCard",["yes","No"])

Education_encoded=0 if Education=="😒undergraduat"else (1 if Education=="😊graduat" else 2 )
Securities_Account_encoder= 1 if Securities_Account=="yes"else 0
CD_Account_encoder=1 if CD_Account=="yes" else 0
Online_encoder=1 if Online=="yes" else 0
CreditCard_encoder= 1 if CreditCard=="yes" else 0

if st.button("Predict"):
    input_data=np.array([[Age,Experince,Income,Family,CCAvg,Education_encoded,Mortgage,Securities_Account_encoder,CD_Account_encoder,Online_encoder,CreditCard_encoder]])
    prediction=model.predict(input_data)[0]

    if prediction==1:
        st.success("prediction: Aplicabel for loan")
    else:
        st.error("pridiction: Not aplicabel for loan")

        