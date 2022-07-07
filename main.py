from fastapi import FastAPI, Request
from scrapper.controller import scrapCreation, scrapperdetails

app = FastAPI()


@app.get("/{id}")
async def get_data(request: Request, id: int):
    return scrapperdetails(id=id)



@app.post("/create")
async def create_data(request: Request):
    return scrapCreation()
