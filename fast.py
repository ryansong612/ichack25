from fastapi import FastAPI
from models import Grid
from crop import db

app = FastAPI()

@app.get("/")
def read_root():
    print("HI")
    return {"message": "hi"}

@app.get("/get_all_crops")
def supported():
    return {"supported": list(db.keys())}

@app.get("/state/")
def read_item(grid: Grid):
    print("Hi")
    return {"item_id": grid}

@app.post("/send/")
def send_updated(grid: Grid):
    return grid

