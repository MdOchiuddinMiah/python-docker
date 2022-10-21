from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/departments/{student_id}")
def read_item(student_id: int, q: Optional[str] = None):
    return {"department_id":23, "student_id": student_id, "name": q}
