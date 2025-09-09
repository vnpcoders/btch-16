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
    Education: Annotated[Literal["😒undergraduat","😊graduat","😂postgraduat"], Field(...,description="Education select only 😒undergraduat,😊graduat,😂postgraduat")]
    Mortgage: Annotated[int, Field(...,gt = 0,description="Mortgage")]
    Securities_Account: Annotated[Literal["YES","NO"], Field(..., description="Securities_Account")]
    CD_Account: Annotated[Literal["YES","NO"], Field(..., description="CD_Account")]
    Online: Annotated[Literal["YES","NO"], Field(..., description="Online")]
    CreditCard: Annotated[Literal["YES","NO"], Field(..., description="CreditCard")]


Education_encoded=0 if Passenger.Education=="😒undergraduat"else (1 if Passenger.Education=="😊graduat" else 2 )
Securities_Account_encoder= 1 if Passenger.Securities_Account=="yes"else 0
CD_Account_encoder=1 if Passenger.CD_Account=="yes" else 0
Online_encoder=1 if Passenger.Online=="yes" else 0
CreditCard_encoder= 1 if Passenger.CreditCard=="yes" else 0

if st.button("Predict"):
    input_data=np.array([[Age,Experince,Income,Family,CCAvg,Education_encoded,Mortgage,Securities_Account_encoder,CD_Account_encoder,Online_encoder,CreditCard_encoder]])
    prediction=model.predict(input_data)[0]

    if prediction==1:
        st.success("prediction: Aplicabel for loan")
    else:
        st.error("pridiction: Not aplicabel for loan")

        