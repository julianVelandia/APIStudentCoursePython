from fastapi import APIRouter

from src.app.wire import new_wire_view_profile, new_wire_view_class
from src.handler.classes.contract.request import ClassesRequest
from src.handler.student.contract.request import StudentRequest

student_router = APIRouter()


@student_router.get("/v1.0/student/profile/{email}")
async def handler_view_student_profile(email: str):
    request = StudentRequest(email=email)
    return new_wire_view_profile(request)


classes_router = APIRouter()

@classes_router.get("/v1.0/classes/class/{class_id}/email/{email}/title/{title}")
async def handler_view_class(class_id: str, email: str, title: str):
    request = ClassesRequest(
        class_id=class_id,
        email=email,
        title=title)
    return new_wire_view_class(request)
