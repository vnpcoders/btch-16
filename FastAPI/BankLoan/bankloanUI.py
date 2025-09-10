from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import pickle
import pandas as pd

model = pickle.load(open("rf_model.pkl", "rb"))

app = FastAPI(title="CHECK ELIGIBILITY FOR LOAN AMOUNT")

class BankLoan(BaseModel):
    Age: Annotated[int, Field(..., gt=18, lt=80, description="Age of the Applicant")]
    Experience: Annotated[int, Field(..., gt=0, description="Experience")]
    Income: Annotated[int, Field(..., gt=0, description="Income")]
    Family: Annotated[int, Field(..., gt=1, lt=20, description="Family Members")]
    CCAvg: Annotated[int, Field(..., gt=0, description="CCAvg")]
    Education: Annotated[Literal["undergraduat", "graduat", "postgraduat"], Field(..., description="Education")]
    Mortgage: Annotated[int, Field(..., gt=0, description="Mortgage")]
    Securities_Account: Annotated[Literal["YES", "NO"], Field(..., description="Securities Account")]
    CD_Account: Annotated[Literal["YES", "NO"], Field(..., description="CD Account")]
    Online: Annotated[Literal["YES", "NO"], Field(..., description="Online Banking")]
    CreditCard: Annotated[Literal["YES", "NO"], Field(..., description="Credit Card")]

@app.post("/predict")
def predict_loan(bankloan: BankLoan):
    # Encode categorical fields
    Education_encoded = 0 if bankloan.Education == "undergraduat" else (1 if bankloan.Education == "graduat" else 2)
    Securities_Account_encoded = 1 if bankloan.Securities_Account == "YES" else 0
    CD_Account_encoded = 1 if bankloan.CD_Account == "YES" else 0
    Online_encoded = 1 if bankloan.Online == "YES" else 0
    CreditCard_encoded = 1 if bankloan.CreditCard == "YES" else 0

    # Create input DataFrame
    input_df = pd.DataFrame([{
        "Age": bankloan.Age,
        "Experience": bankloan.Experience,
        "Income": bankloan.Income,
        "Family": bankloan.Family,
        "CCAvg": bankloan.CCAvg,
        "Education": Education_encoded,
        "Mortgage": bankloan.Mortgage,
        "Securities_Account": Securities_Account_encoded,
        "CD_Account": CD_Account_encoded,
        "Online": Online_encoded,
        "CreditCard": CreditCard_encoded,
    }])

    # Rename columns to match training
    input_df = input_df.rename(columns={
        "Securities_Account": "Securities.Account",
        "CD_Account": "CD.Account"
    })

    # Predict
    prediction = model.predict(input_df)[0]
    return {"Applicable or not": int(prediction)}
