from fastapi import FastAPI
from pydantic import BaseModel
from main import main

app = FastAPI()

class CropsModel(BaseModel):
    cropData: dict[str, dict[str, float]]
    location: str
    curr_month: int

@app.post("/send")
def send_updated(req: CropsModel):
    return main(req.location, req.curr_month, req.cropData) # return updated percentages