from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

subtasks_router = APIRouter()


@subtasks_router.post("/subtasks/", response_model=schemas.Subtask)
def create_subtask(subtask: schemas.SubtaskCreate, db: Session = Depends(get_db)):
    return crud.create_subtask(db, subtask)


@subtasks_router.get("/subtasks/{subtask_id}", response_model=schemas.Subtask)
def read_subtask(subtask_id: int, db: Session = Depends(get_db)):
    db_subtask = crud.get_subtask(db, subtask_id)
    if db_subtask is None:
        raise HTTPException(status_code=404, detail="Subtask not found")
    return db_subtask


@subtasks_router.get("/subtasks/", response_model=list[schemas.Subtask])
def read_subtasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subtasks = crud.get_subtasks(db, skip=skip, limit=limit)
    return subtasks


@subtasks_router.put("/subtasks/{subtask_id}", response_model=schemas.Subtask)
def update_subtask(subtask_id: int, subtask: schemas.SubtaskCreate, db: Session = Depends(get_db)):
    db_subtask = crud.get_subtask(db, subtask_id)
    if db_subtask is None:
        raise HTTPException(status_code=404, detail="Subtask not found")
    return crud.update_subtask(db, db_subtask, subtask)


@subtasks_router.delete("/subtasks/{subtask_id}", response_model=schemas.Subtask)
def delete_subtask(subtask_id: int, db: Session = Depends(get_db)):
    db_subtask = crud.get_subtask(db, subtask_id)
    if db_subtask is None:
        raise HTTPException(status_code=404, detail="Subtask not found")
    return crud.delete_subtask(db, db_subtask)