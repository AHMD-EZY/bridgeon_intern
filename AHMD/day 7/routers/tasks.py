from fastapi import APIRouter, HTTPException, Query

from database import (
    create_task,
    get_tasks,
    update_task,
    delete_task
)

from models import TaskCreate, TaskUpdate

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)
@router.post("/")
def add_task(task: TaskCreate):
    return create_task(task.title)
@router.get("/")
def list_tasks(
    status: str | None = Query(
        default=None,
        description="pending or completed"
    )
):
    return get_tasks(status)
@router.put("/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):

    updated = update_task(
        task_id,
        task.title,
        task.completed
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated
@router.delete("/{task_id}")
def remove_task(task_id: int):

    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted"}
