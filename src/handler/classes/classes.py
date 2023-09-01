from http.client import HTTPException

from internal.classes.application.query.view import View
from internal.classes.domain.classes import Classes
from src.handler.classes.contract.request import ClassesRequest
from src.handler.classes.contract.response import ClassesResponse


class ClassesMapper:
    def request_to_query(self, request: ClassesRequest) -> View:
        pass

    def domain_to_response(self, class_instance: Classes) -> ClassesResponse:
        pass


class UseCase:
    def execute(self, qry: View) -> Classes:
        pass


class HandlerViewClass(ClassesMapper, UseCase):
    def __init__(self, mapper: ClassesMapper, use_case: UseCase):
        self.mapper = mapper
        self.use_case = use_case

    def handler_view_class(self, request: ClassesRequest) -> ClassesResponse:
        try:
            qry = self.mapper.request_to_query(request)
        except Exception:
            raise HTTPException(status_code=400, detail="Bad Request")

        try:
            domain_class = self.use_case.execute(qry)
        except Exception:
            raise HTTPException(status_code=500, detail="Internal Server Error")

        response = self.mapper.domain_to_response(domain_class)
        return response
