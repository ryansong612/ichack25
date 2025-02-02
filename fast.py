from fastapi import FastAPI
from pydantic import BaseModel
from main import main

app = FastAPI()

class CropsModel(BaseModel):
    percentages: dict[str, float]
    location: str
    curr_month: int

@app.post("/send/", response_model=CropsModel)
def send_updated(req: CropsModel):
    main(req)
    data = {
    "percentages": {"wheat": 75.5, "corn": 60.2},
    "location": "Texas",
    "curr_month": 2
    }
    return data
