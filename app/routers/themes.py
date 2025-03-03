from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

themes_router = APIRouter()


@themes_router.post("/themes/", response_model=schemas.Theme)
def create_theme(theme: schemas.ThemeCreate, db: Session = Depends(get_db)):
    return crud.create_theme(db, theme)

@themes_router.get("/themes/{theme_id}", response_model=schemas.Theme)
def read_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = crud.get_theme(db, theme_id)
    if db_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return db_theme

@themes_router.get("/themes/", response_model=list[schemas.Theme])
def read_themes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = crud.get_themes(db, skip=skip, limit=limit)
    return tasks



@themes_router.post("/theme-params/", response_model=schemas.ThemeParam)
def create_theme_param(theme_param: schemas.ThemeParamCreate, db: Session = Depends(get_db)):
    return crud.create_theme_param(db, theme_param)

@themes_router.get("/theme-params/{theme_id}", response_model=list[schemas.ThemeParam])
def read_theme_params(theme_id: int, db: Session = Depends(get_db)):
    theme_params = crud.get_theme_params(db, theme_id)
    if not theme_params:
        raise HTTPException(status_code=404, detail="Theme params not found")
    return theme_params

@themes_router.delete("/theme-params/{theme_param_id}", response_model=schemas.ThemeParam)
def delete_theme_param(theme_param_id: int, db: Session = Depends(get_db)):
    db_theme_param = crud.delete_theme_param(db, theme_param_id)
    if db_theme_param is None:
        raise HTTPException(status_code=404, detail="Theme param not found")
    return db_theme_param