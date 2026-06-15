from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

tasks = {}

# Create Schema
class TaskCreate(BaseModel):
    title: str

# Update Schema
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

# Response Schema
class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool


# POST Create Task
@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate):

    task_id = len(tasks) + 1

    tasks[task_id] = {
        "id": task_id,
        "title": task.title,
        "completed": False
    }

    return tasks[task_id]


# GET All Tasks
@router.get("/", response_model=list[TaskResponse])
def get_tasks():
    return list(tasks.values())


# GET One Task
@router.get("/{id}", response_model=TaskResponse)
def get_task(id: int):

    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return tasks[id]


# PUT Update Task
@router.put("/{id}", response_model=TaskResponse)
def update_task(id: int, task: TaskUpdate):

    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.title is not None:
        tasks[id]["title"] = task.title

    if task.completed is not None:
        tasks[id]["completed"] = task.completed

    return tasks[id]


# DELETE Task
@router.delete("/{id}")
def delete_task(id: int):

    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    del tasks[id]

    return {"message": "Task deleted"}


# BONUS PATCH
@router.patch("/{id}/complete")
def complete_task(id: int):

    if id not in tasks:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    tasks[id]["completed"] = True

    return tasks[id]