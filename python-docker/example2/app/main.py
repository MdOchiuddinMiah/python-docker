from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/students/{id}")
def read_item(id: int, q: Optional[str] = None):
    return {"student_id": id, "name": q, "cgpa": 3.65}
