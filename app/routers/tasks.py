from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

tasks_router = APIRouter()


@tasks_router.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


@tasks_router.get("/tasks/", response_model=List[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db, skip=skip, limit=limit)
    return tasks

@tasks_router.get("/tasks/{task_id}", response_model=schemas.Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, task_id=task_id)
    return task


@tasks_router.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.update_task(db, db_task, task)


@tasks_router.delete("/tasks/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return crud.delete_task(db, db_task)





@tasks_router.post("/task-params/", response_model=schemas.TaskParam)
def create_task_param(task_param: schemas.TaskParamCreate, db: Session = Depends(get_db)):
    return crud.create_task_param(db, task_param)

@tasks_router.get("/task-params/{task_id}", response_model=List[schemas.TaskParam])
def read_task_params(task_id: int, db: Session = Depends(get_db)):
    task_params = crud.get_task_params(db, task_id)
    if not task_params:
        raise HTTPException(status_code=404, detail="Task params not found")
    return task_params

@tasks_router.delete("/task-params/{task_param_id}", response_model=schemas.TaskParam)
def delete_task_param(task_param_id: int, db: Session = Depends(get_db)):
    db_task_param = crud.delete_task_param(db, task_param_id)
    if db_task_param is None:
        raise HTTPException(status_code=404, detail="Task param not found")
    return db_task_param