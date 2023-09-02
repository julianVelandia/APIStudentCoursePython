import uvicorn
from fastapi import FastAPI

from src.app.router import student_router, classes_router

app = FastAPI()
app.include_router(student_router)
app.include_router(classes_router)

if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8080)




