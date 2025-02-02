from fastapi import FastAPI
from pydantic import BaseModel
from main import main
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",  # React dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CropsModel(BaseModel):
    cropData: dict[str, dict[str, float]]
    location: str
    curr_month: int

@app.post("/send")
def send_updated(req: CropsModel):
    return main(req.location, req.curr_month, req.cropData) # return updated percentages