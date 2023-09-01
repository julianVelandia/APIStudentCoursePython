from pydantic import BaseModel


class ClassesRequest(BaseModel):
    email: str
    class_id: str
    title: str
