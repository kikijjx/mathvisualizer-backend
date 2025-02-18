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