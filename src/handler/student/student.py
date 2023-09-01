from http.client import HTTPException

from internal.student.application.query.view import View
from internal.student.domain.profile import Profile
from src.handler.student.contract.request import StudentRequest
from src.handler.student.contract.response import StudentResponse


class StudentMapper:
    def request_to_query(self, request: StudentRequest) -> View:
        pass

    def domain_to_response(self, profile: Profile) -> StudentResponse:
        pass


class UseCase:
    def execute(self, email: str) -> Profile:
        pass


class HandlerViewProfile(StudentMapper, UseCase):
    def __init__(self, mapper: StudentMapper, use_case: UseCase):
        self.mapper = mapper
        self.use_case = use_case

    def handler_view_profile(self, request: StudentRequest) -> StudentResponse:
        try:
            qry = self.mapper.request_to_query(request)
        except Exception:
            raise HTTPException(status_code=400, detail="Bad Request")

        try:
            domain_profile = self.use_case.execute(qry.email)
        except Exception:
            raise HTTPException(status_code=500, detail="Internal Server Error")

        response = self.mapper.domain_to_response(domain_profile)
        return response
