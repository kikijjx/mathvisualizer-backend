from fastapi import FastAPI
from app.routers.themes import themes_router
from app.routers.methods import methods_router
from app.routers.subtasks import subtasks_router
from app.routers.tasks import tasks_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(themes_router,   prefix="/api")
app.include_router(methods_router,  prefix="/api")
app.include_router(subtasks_router, prefix="/api")
app.include_router(tasks_router,    prefix="/api")


