from typing import Union
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "111We Love Datascientest 3, and we did it. We build a CI/CD Pipeline !!"}
