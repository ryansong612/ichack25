from fastapi import FastAPI
from pydantic import BaseModel
from main import main

app = FastAPI()

class CropsModel(BaseModel):
    percentages: dict[str, float]
    location: str
    curr_month: int

@app.post("/get_all_crops")
def get_crop_percentages(req: CropsModel):
    print(req)
    return main(req)

@app.post("/send/", response_model=CropsModel)
def send_updated(updated_percentages, location, curr_month):
    crop_data = CropsModel(updated_percentages, location, curr_month)
    return crop_data
