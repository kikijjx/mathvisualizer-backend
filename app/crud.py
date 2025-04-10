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


def create_theme_param(db: Session, theme_param: schemas.ThemeParamCreate):
    db_theme_param = models.ThemeParam(**theme_param.dict())
    db.add(db_theme_param)
    db.commit()
    db.refresh(db_theme_param)
    return db_theme_param

def get_theme_params(db: Session, theme_id: int):
    return db.query(models.ThemeParam).filter(models.ThemeParam.theme_id == theme_id).all()

def get_theme_param(db: Session, theme_param_id: int):
    return db.query(models.ThemeParam).filter(models.ThemeParam.id == theme_param_id).first()

def delete_theme_param(db: Session, theme_param_id: int):
    db_theme_param = db.query(models.ThemeParam).filter(models.ThemeParam.id == theme_param_id).first()
    if db_theme_param:
        db.delete(db_theme_param)
        db.commit()
    return db_theme_param

# TaskParams CRUD
def create_task_param(db: Session, task_param: schemas.TaskParamCreate):
    db_task_param = models.TaskParam(**task_param.dict())
    db.add(db_task_param)
    db.commit()
    db.refresh(db_task_param)
    return db_task_param

def get_task_params(db: Session, task_id: int):
    return db.query(models.TaskParam).filter(models.TaskParam.task_id == task_id).all()

def get_task_param(db: Session, task_param_id: int):
    return db.query(models.TaskParam).filter(models.TaskParam.id == task_param_id).first()

def delete_task_param(db: Session, task_param_id: int):
    db_task_param = db.query(models.TaskParam).filter(models.TaskParam.id == task_param_id).first()
    if db_task_param:
        db.delete(db_task_param)
        db.commit()
    return db_task_param


def create_method_param(db: Session, method_param: schemas.MethodParamCreate):
    db_method_param = models.MethodParam(**method_param.dict())
    db.add(db_method_param)
    db.commit()
    db.refresh(db_method_param)
    return db_method_param

def get_method_params_by_method(db: Session, method_id: int):
    return db.query(models.MethodParam).filter(models.MethodParam.method_id == method_id).all()

def get_method_param(db: Session, param_id: int):
    return db.query(models.MethodParam).filter(models.MethodParam.id == param_id).first()

def update_method_param(db: Session, db_param: models.MethodParam, method_param: schemas.MethodParamCreate):
    for key, value in method_param.dict().items():
        setattr(db_param, key, value)
    db.commit()
    db.refresh(db_param)
    return db_param

def delete_method_param(db: Session, db_param: models.MethodParam):
    db.delete(db_param)
    db.commit()
    return db_param


def create_report_template(db: Session, report_template: schemas.ReportTemplateCreate):
    # Преобразуем список ReportContent в список словарей
    content_dict = [item.dict() for item in report_template.content]
    
    db_report_template = models.ReportTemplate(
        task_id=report_template.task_id,
        name=report_template.name,
        content=content_dict  # Передаём сериализованный список
    )
    db.add(db_report_template)
    db.commit()
    db.refresh(db_report_template)
    return db_report_template

def get_report_template(db: Session, report_template_id: int):
    return db.query(models.ReportTemplate).filter(models.ReportTemplate.id == report_template_id).first()

def get_report_templates(db: Session, task_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.ReportTemplate)
        .filter(models.ReportTemplate.task_id == task_id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def update_report_template(db: Session, db_report_template: models.ReportTemplate, report_template: schemas.ReportTemplateCreate):
    # Преобразуем список ReportContent в список словарей
    content_dict = [item.dict() for item in report_template.content]
    
    db_report_template.task_id = report_template.task_id
    db_report_template.name = report_template.name
    db_report_template.content = content_dict  # Обновляем content как список словарей
    db.commit()
    db.refresh(db_report_template)
    return db_report_template

def delete_report_template(db: Session, db_report_template: models.ReportTemplate):
    db.delete(db_report_template)
    db.commit()
    return db_report_template