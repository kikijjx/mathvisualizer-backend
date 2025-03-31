from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from app.database import Base

class Theme(Base):
    __tablename__ = "themes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    methods = relationship("Method", back_populates="theme")
    params = relationship("ThemeParam", back_populates="theme")


class ThemeParam(Base):
    __tablename__ = "theme_params"
    id = Column(Integer, primary_key=True, index=True)
    theme_id = Column(Integer, ForeignKey("themes.id"), nullable=False)
    name = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)
    default_value = Column(String, nullable=True)
    theme = relationship("Theme", back_populates="params")

class Method(Base):
    __tablename__ = "methods"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    theme_id = Column(Integer, ForeignKey("themes.id"))

    theme = relationship("Theme", back_populates="methods")
    params = relationship("MethodParam", back_populates="method")

class MethodParam(Base):
    __tablename__ = "method_params"
    id = Column(Integer, primary_key=True, index=True)
    method_id = Column(Integer, ForeignKey("methods.id"))
    name = Column(String)
    type = Column(String)
    default_value = Column(String)

    method = relationship("Method", back_populates="params")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    theme_id = Column(Integer, ForeignKey("themes.id"))
    description = Column(String, index=True)
    subtasks = relationship("Subtask", back_populates="task", cascade="all, delete-orphan")
    params = relationship("TaskParam", back_populates="task", cascade="all, delete-orphan")
    report_templates = relationship("ReportTemplate", back_populates="task", cascade="all, delete-orphan")

class TaskParam(Base):
    __tablename__ = "task_params"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    param_name = Column(String(255), nullable=False)
    param_value = Column(String, nullable=True)
    task = relationship("Task", back_populates="params")

class Subtask(Base):
    __tablename__ = "subtasks"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    method_id = Column(Integer, ForeignKey("methods.id"))
    params = Column(JSON)

    task = relationship("Task", back_populates="subtasks")
    method = relationship("Method")

class ReportTemplate(Base):
    __tablename__ = "report_templates"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    name = Column(String, index=True)  # Название шаблона
    content = Column(JSON, nullable=False)  # Содержимое шаблона (текст, таблицы, изображения)

    task = relationship("Task", back_populates="report_templates")

    