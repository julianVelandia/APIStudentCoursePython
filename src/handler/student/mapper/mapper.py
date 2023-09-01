from internal.student.application.query.view import View
from internal.student.domain.profile import Profile
from src.handler.student.contract.request import StudentRequest
from src.handler.student.contract.response import StudentResponse, StudentClass


class StudentMapper:
    @staticmethod
    def domain_to_response(profile: Profile):
        classes_done_response = []
        for class_done in profile.classes():
            classes_done_response.append(
                StudentClass(
                    class_id=class_done.class_id,
                    title=class_done.title
                )
            )
        return StudentResponse(
            email=profile.email,
            name=profile.name,
            classes_done=classes_done_response
        )

    @staticmethod
    def request_to_query(request: StudentRequest):
        return View(
            email=request.email,
        )
