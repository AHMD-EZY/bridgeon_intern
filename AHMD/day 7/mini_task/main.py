from fastapi import FastAPI
from pydantic import BaseModel

from db import create_table, add_task, get_tasks

app = FastAPI()

create_table()


class Task(BaseModel):
    title: str


@app.post("/tasks")
def create_task(task: Task):
    return add_task(task.title)


@app.get("/tasks")
def read_tasks():
    return get_tasks()