from pydantic import BaseModel
from typing import List, Optional

class ThemeParamBase(BaseModel):
    name: str
    type: str
    default_value: Optional[str] = None

class ThemeParamCreate(ThemeParamBase):
    theme_id: int

class ThemeParam(ThemeParamBase):
    id: int
    theme_id: int

    class Config:
        orm_mode = True

class ThemeBase(BaseModel):
    name: str

class ThemeCreate(ThemeBase):
    pass

class Theme(ThemeBase):
    id: int
    params: List[ThemeParam] = []

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
    params: List[MethodParam] = []

    class Config:
        orm_mode = True

class SubtaskBase(BaseModel):
    task_id: int
    method_id: int
    params: Optional[dict] = None

class SubtaskCreate(SubtaskBase):
    pass

class Subtask(SubtaskBase):
    id: int

    class Config:
        orm_mode = True

class TaskParamBase(BaseModel):
    param_name: str
    param_value: Optional[str] = None

class TaskParamCreate(TaskParamBase):
    task_id: int

class TaskParam(TaskParamBase):
    id: int
    task_id: int

    class Config:
        orm_mode = True

class TaskBase(BaseModel):
    name: str
    description: str
    theme_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    subtasks: List[Subtask] = []
    params: List[TaskParam] = []

    class Config:
        orm_mode = True