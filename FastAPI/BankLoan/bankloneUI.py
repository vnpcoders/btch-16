from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Annotated,Literal
import pickle
import pandas as pd

model=pickle.load(open("rf_model.pkl","rb"))

app = FastAPI(title="CHECK ELEGIBLITY FOR LOAN AMOUNT ")


class banklone(BaseModel):
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

@app.post("/predict")
def predict_lone(banklone: banklone):
    # Encode categorical fields
    Education_encoded=0 if banklone.Education=="😒undergraduat"else (1 if banklone  .Education=="😊graduat" else 2 )
    Securities_Account_encoder= 1 if banklone.Securities_Account=="yes"else 0
    CD_Account_encoder=1 if banklone.CD_Account=="yes" else 0
    Online_encoder=1 if banklone.Online=="yes" else 0
    CreditCard_encoder= 1 if banklone.CreditCard=="yes" else 0

    # Create input DataFrame
    input_df = pd.DataFrame([{
        "Pclass": banklone.Age,
        "Sex": sex_encoded,
        "Age": banklone.Age,
        "SibSp": banklone.SibSp,
        "Parch": passengerbanklone.Parch,
        "Fare": passenger.Fare,
        "Embarked": embarked_encoded
    }])

        