from pydantic import BaseModel


class StudentRequest(BaseModel):
    email: str