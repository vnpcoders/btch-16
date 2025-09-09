from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Annotated,Literal
import pickle
import pandas as pd

model=pickle.load(open("rf_model.pkl","rb"))

app = FastAPI(title="CHECK ELEGIBLITY FOR LOAN AMOUNT ")


class Passenger(BaseModel):
    Age: Annotated[int, Field(..., gt = 18, lt = 80,description="Age of the Passenger")]
    Experience: Annotated[int, Field(..., gt = 0,description="Experience")]
    Income: Annotated[int, Field(...,gt = 0,description="Income")]
    Family: Annotated[int, Field(...,gt = 1, lt = 20,description="Family Members")]
    CCAvg: Annotated[int, Field(..., gt = 0,description="CCAvg")]

    Income: Annotated[Literal["S","C","Q"], Field(...,gt = 0,description="Income")]
    Mortgage: Annotated[int, Field(...,gt = 0,description="Mortgage")]

    Embarked: Annotated[Literal["S","C","Q"], Field(..., description="Age of the user")]
"""




Education=st.selectbox("Education",["😒undergraduat","😊graduat","😂postgraduat"])

Securities_Account=st.selectbox("Securities_Account",["yes","No"])
CD_Account=st.selectbox("CD_Account",["yes","No"])
Online=st.selectbox("Online",["yes","No"])
CreditCard=st.selectbox("CreditCard",["yes","No"])"""

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

        