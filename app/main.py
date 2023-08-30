from fastapi import FastAPI
from src.handler.classes.view.handler import router as classes_router
from src.handler.student.view.handler import router as student_router


app = FastAPI()
app.include_router(classes_router)
app.include_router(student_router)
