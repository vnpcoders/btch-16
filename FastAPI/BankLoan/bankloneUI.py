# from fastapi import FastAPI
# from pydantic import BaseModel, Field, computed_field
# from typing import Annotated,Literal
# import pickle
# import pandas as pd

# model=pickle.load(open("rf_model.pkl","rb"))

# app = FastAPI(title="CHECK ELEGIBLITY FOR LOAN AMOUNT ")


# class banklone(BaseModel):
#     Age: Annotated[int, Field(..., gt = 18, lt = 80,description="Age of the Passenger")]
#     Experience: Annotated[int, Field(..., gt = 0,description="Experience")]
#     Income: Annotated[int, Field(...,gt = 0,description="Income")]
#     Family: Annotated[int, Field(...,gt = 1, lt = 20,description="Family Members")]
#     CCAvg: Annotated[int, Field(..., gt = 0,description="CCAvg")]
#     Education: Annotated[Literal["undergraduat","graduat","postgraduat"], Field(...,description="Education select only 😒undergraduat,😊graduat,😂postgraduat")]
#     Mortgage: Annotated[int, Field(...,gt = 0,description="Mortgage")]
#     Securities_Account: Annotated[Literal["YES","NO"], Field(..., description="Securities_Account")]
#     CD_Account: Annotated[Literal["YES","NO"], Field(..., description="CD_Account")]
#     Online: Annotated[Literal["YES","NO"], Field(..., description="Online")]
#     CreditCard: Annotated[Literal["YES","NO"], Field(..., description="CreditCard")]

# @app.post("/predict")
# def predict_lone(banklone: banklone):
#     # Encode categorical fields
#     Education_encoded=0 if banklone.Education=="undergraduat"else (1 if banklone  .Education=="graduat" else 2 )
#     Securities_Account_encoder= 1 if banklone.Securities_Account=="YES"else 0
#     CD_Account_encoder=1 if banklone.CD_Account=="YES" else 0
#     Online_encoder=1 if banklone.Online=="YES" else 0
#     CreditCard_encoder= 1 if banklone.CreditCard=="YES" else 0

#     # Create input DataFrame
#     input_df = pd.DataFrame([{
#         "Age": banklone.Age,
#         "Experience": banklone.Experience,
#         "Income": banklone.Income,
#         "Family": banklone.Family,
#         "CCAvg": banklone.CCAvg,
#         "Education": Education_encoded,
#         "Mortgage": banklone.Mortgage,
#         "Securities_Account": Securities_Account_encoder,
#         "CD_Account": CD_Account_encoder,
#         "Online": Online_encoder,
#         "CreditCard": CreditCard_encoder,


#     }])

#     # Predict
#     prediction = model.predict(input_df)[0]
#     return {"Aplicable or not": int(prediction)}
        

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated, Literal
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("rf_model.pkl", "rb"))

app = FastAPI(title="CHECK ELIGIBILITY FOR LOAN AMOUNT")

class BankLoanInput(BaseModel):
    Age: Annotated[int, Field(..., gt=18, lt=80, description="Age of the Applicant")]
    Experience: Annotated[int, Field(..., ge=0, description="Work experience in years")]
    Income: Annotated[int, Field(..., gt=0, description="Annual Income (in $1000s)")]
    Family: Annotated[int, Field(..., ge=1, le=20, description="Number of family members")]
    CCAvg: Annotated[float, Field(..., ge=0, description="Avg. spending on credit cards per month (in $1000s)")]
    Education: Annotated[
        Literal["undergraduate", "graduate", "postgraduate"], 
        Field(..., description="Education: undergraduate / graduate / postgraduate")
    ]
    Mortgage: Annotated[int, Field(..., ge=0, description="Mortgage Value")]
    Securities_Account: Annotated[Literal["YES", "NO"], Field(..., description="Has Securities Account?")]
    CD_Account: Annotated[Literal["YES", "NO"], Field(..., description="Has Certificate of Deposit Account?")]
    Online: Annotated[Literal["YES", "NO"], Field(..., description="Uses Online Banking?")]
    CreditCard: Annotated[Literal["YES", "NO"], Field(..., description="Has Credit Card issued by bank?")]

@app.post("/predict")
def predict_loan(data: BankLoanInput):
    # Encode categorical fields
    edu_map = {"undergraduate": 1, "graduate": 2, "postgraduate": 3}
    Education_encoded = edu_map[data.Education]

    Securities_Account_encoded = 1 if data.Securities_Account == "YES" else 0
    CD_Account_encoded = 1 if data.CD_Account == "YES" else 0
    Online_encoded = 1 if data.Online == "YES" else 0
    CreditCard_encoded = 1 if data.CreditCard == "YES" else 0

    # Create input DataFrame
    input_df = pd.DataFrame([{
        "Age": data.Age,
        "Experience": data.Experience,
        "Income": data.Income,
        "Family": data.Family,
        "CCAvg": data.CCAvg,
        "Education": Education_encoded,
        "Mortgage": data.Mortgage,
        "Securities_Account": Securities_Account_encoded,
        "CD_Account": CD_Account_encoded,
        "Online": Online_encoded,
        "CreditCard": CreditCard_encoded
    }])

    # Predict
    prediction = model.predict(input_df)[0]
    return {"Applicable": bool(prediction)}
