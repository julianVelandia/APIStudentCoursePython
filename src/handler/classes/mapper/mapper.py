from internal.classes.application.query.view import View
from internal.classes.domain.classes import Classes
from src.handler.classes.contract.request import ClassesRequest
from src.handler.classes.contract.response import ClassesResponse


class ClassesMapper:
    @staticmethod
    def domain_to_response(classes: Classes):
        return ClassesResponse(
            class_id=classes.class_id,
            title=classes.title,
            creation_date=classes.creation_date,
            content=classes.content,
            read_time=classes.read_time
        )

    @staticmethod
    def request_to_query(request: ClassesRequest):
        return View(
            email=request.email,
            class_id=request.class_id,
            title=request.title,
        )
