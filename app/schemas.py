from pydantic import BaseModel
from typing import List, Optional

class ThemeBase(BaseModel):
    name: str

class ThemeCreate(ThemeBase):
    pass

class Theme(ThemeBase):
    id: int

    class Config:
        orm_mode = True

class MethodParamBase(BaseModel):
    name: str
    type: str
    default_value: Optional[str] = None

class MethodParamCreate(MethodParamBase):
    method_id: int

class MethodParam(MethodParamBase):
    id: int

    class Config:
        orm_mode = True

class MethodBase(BaseModel):
    name: str
    description: str
    theme_id: int

class MethodCreate(MethodBase):
    pass

class Method(MethodBase):
    id: int
    params: List[MethodParam] = []  # Добавляем параметры

    class Config:
        orm_mode = True



class SubtaskBase(BaseModel):
    #id: int
    task_id: int
    method_id: int
    params: Optional[dict] = None

class SubtaskCreate(SubtaskBase): 
    pass

class TaskBase(BaseModel):
    name: str
    description: str
    theme_id: int
    subtasks: List[SubtaskBase]

class TaskCreate(TaskBase):
    subtasks: List[SubtaskCreate]



class SubtaskCreate(SubtaskBase):
    pass

class Subtask(SubtaskBase):
    id: int

    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    subtasks: List[Subtask]
    class Config:
        orm_mode = True