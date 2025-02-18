from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

import app.models as models
import app.schemas as schemas


def get_theme(db: Session, theme_id: int):
    return db.query(models.Theme).filter(models.Theme.id == theme_id).first()

def create_theme(db: Session, theme: schemas.ThemeCreate):
    db_theme = models.Theme(name=theme.name)
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme

def get_themes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Theme).offset(skip).limit(limit).all()

def create_method(db: Session, method: schemas.MethodCreate):
    db_method = models.Method(**method.dict())
    db.add(db_method)
    db.commit()
    db.refresh(db_method)
    return db_method

def get_method(db: Session, method_id: int):
    return db.query(models.Method).filter(models.Method.id == method_id).first()

def get_methods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Method).offset(skip).limit(limit).all()

def update_method(db: Session, db_method: models.Method, method: schemas.MethodCreate):
    for key, value in method.dict().items():
        setattr(db_method, key, value)
    db.commit()
    db.refresh(db_method)
    return db_method

def delete_method(db: Session, db_method: models.Method):
    db.delete(db_method)
    db.commit()
    return db_method

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int):
    task = (
        db.query(models.Task)
        .options(joinedload(models.Task.subtasks))
        .filter(models.Task.id == task_id)
        .first()
    )
    return task

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = (
        db.query(models.Task)
        .options(joinedload(models.Task.subtasks))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return tasks

def update_task(db: Session, db_task: models.Task, task: schemas.TaskCreate):
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, db_task: models.Task):
    db.delete(db_task)
    db.commit()
    return db_task

def create_subtask(db: Session, subtask: schemas.SubtaskCreate):
    db_subtask = models.Subtask(**subtask.dict())
    db.add(db_subtask)
    db.commit()
    db.refresh(db_subtask)
    return db_subtask

def get_subtask(db: Session, subtask_id: int):
    return db.query(models.Subtask).filter(models.Subtask.id == subtask_id).first()

def get_subtasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Subtask).offset(skip).limit(limit).all()

def update_subtask(db: Session, db_subtask: models.Subtask, subtask: schemas.SubtaskCreate):
    for key, value in subtask.dict().items():
        setattr(db_subtask, key, value)
    db.commit()
    db.refresh(db_subtask)
    return db_subtask

def delete_subtask(db: Session, db_subtask: models.Subtask):
    db.delete(db_subtask)
    db.commit()
    return db_subtask
