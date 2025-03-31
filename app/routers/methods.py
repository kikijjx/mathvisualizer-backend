from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud
import app.models as models
methods_router = APIRouter()

@methods_router.post("/methods/", response_model=schemas.Method)
def create_method(method: schemas.MethodCreate, db: Session = Depends(get_db)):
    return crud.create_method(db, method)

@methods_router.get("/methods/{method_id}", response_model=schemas.Method)
def read_method(method_id: int, db: Session = Depends(get_db)):
    db_method = crud.get_method(db, method_id)
    if db_method is None:
        raise HTTPException(status_code=404, detail="Method not found")
    return db_method

@methods_router.get("/methods/", response_model=list[schemas.Method])
def read_methods(theme_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if theme_id is not None:
        methods = db.query(models.Method).filter(models.Method.theme_id == theme_id).offset(skip).limit(limit).all()
    else:
        methods = crud.get_methods(db, skip=skip, limit=limit)
    return methods

@methods_router.put("/methods/{method_id}", response_model=schemas.Method)
def update_method(method_id: int, method: schemas.MethodCreate, db: Session = Depends(get_db)):
    db_method = crud.get_method(db, method_id)
    if db_method is None:
        raise HTTPException(status_code=404, detail="Method not found")
    return crud.update_method(db, db_method, method)

@methods_router.delete("/methods/{method_id}", response_model=schemas.Method)
def delete_method(method_id: int, db: Session = Depends(get_db)):
    db_method = crud.get_method(db, method_id)
    if db_method is None:
        raise HTTPException(status_code=404, detail="Method not found")
    return crud.delete_method(db, db_method)

@methods_router.post("/methods/{method_id}/params/", response_model=schemas.MethodParam)
def create_method_param(method_id: int, method_param: schemas.MethodParamCreate, db: Session = Depends(get_db)):
    db_method = crud.get_method(db, method_id)
    if db_method is None:
        raise HTTPException(status_code=404, detail="Method not found")
    return crud.create_method_param(db, method_param)

@methods_router.get("/methods/{method_id}/params/", response_model=list[schemas.MethodParam])
def read_method_params(method_id: int, db: Session = Depends(get_db)):
    db_method = crud.get_method(db, method_id)
    if db_method is None:
        raise HTTPException(status_code=404, detail="Method not found")
    return crud.get_method_params_by_method(db, method_id)

@methods_router.get("/method-params/{param_id}", response_model=schemas.MethodParam)
def read_method_param(param_id: int, db: Session = Depends(get_db)):
    db_param = crud.get_method_param(db, param_id)
    if db_param is None:
        raise HTTPException(status_code=404, detail="Method parameter not found")
    return db_param

@methods_router.put("/method-params/{param_id}", response_model=schemas.MethodParam)
def update_method_param(param_id: int, method_param: schemas.MethodParamCreate, db: Session = Depends(get_db)):
    db_param = crud.get_method_param(db, param_id)
    if db_param is None:
        raise HTTPException(status_code=404, detail="Method parameter not found")
    return crud.update_method_param(db, db_param, method_param)

@methods_router.delete("/method-params/{param_id}", response_model=schemas.MethodParam)
def delete_method_param(param_id: int, db: Session = Depends(get_db)):
    db_param = crud.get_method_param(db, param_id)
    if db_param is None:
        raise HTTPException(status_code=404, detail="Method parameter not found")
    return crud.delete_method_param(db, db_param)