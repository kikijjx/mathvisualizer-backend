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

@tasks_router.post("/report-templates/", response_model=schemas.ReportTemplate)
def create_report_template_endpoint(report_template: schemas.ReportTemplateCreate, db: Session = Depends(get_db)):
    return crud.create_report_template(db, report_template)

@tasks_router.get("/report-templates/{task_id}", response_model=List[schemas.ReportTemplate])
def read_report_templates(task_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    report_templates = crud.get_report_templates(db, task_id, skip=skip, limit=limit)
    return report_templates  # Возвращаем пустой список, если ничего не найдено

@tasks_router.get("/report-template/{report_template_id}", response_model=schemas.ReportTemplate)
def read_report_template(report_template_id: int, db: Session = Depends(get_db)):
    report_template = crud.get_report_template(db, report_template_id)
    if report_template is None:
        raise HTTPException(status_code=404, detail="Report template not found")
    return report_template

@tasks_router.put("/report-templates/{report_template_id}", response_model=schemas.ReportTemplate)
def update_report_template_endpoint(report_template_id: int, report_template: schemas.ReportTemplateCreate, db: Session = Depends(get_db)):
    db_report_template = crud.get_report_template(db, report_template_id)
    if db_report_template is None:
        raise HTTPException(status_code=404, detail="Report template not found")
    return crud.update_report_template(db, db_report_template, report_template)

@tasks_router.delete("/report-templates/{report_template_id}", response_model=schemas.ReportTemplate)
def delete_report_template_endpoint(report_template_id: int, db: Session = Depends(get_db)):
    db_report_template = crud.get_report_template(db, report_template_id)
    if db_report_template is None:
        raise HTTPException(status_code=404, detail="Report template not found")
    return crud.delete_report_template(db, db_report_template)