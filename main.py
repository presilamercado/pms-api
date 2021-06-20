from fastapi import FastAPI
from models import models
from core.database import engine
from core.config import PROJECT_NAME, VERSION
from routes.router import router as api_router
app = FastAPI(title=PROJECT_NAME, version=VERSION)

models.Base.metadata.create_all(engine)

app.include_router(api_router)



# @app.get("/")
# def read_root():
#     return { "api": PROJECT_NAME, "version": VERSION, "docs_path": "/docs" }
#
#
# @app.get("/patients/{patient_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"patient": patient_id, "q": q}