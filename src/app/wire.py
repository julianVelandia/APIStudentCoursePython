from internal.classes.application.usecase.view import ClassesUseCase
from internal.student.application.usecase.view_profile import StudentUseCase
from src.handler.classes.classes import HandlerViewClass, ClassesMapper
from src.handler.student.contract.request import StudentRequest
from src.handler.student.mapper.mapper import StudentMapper
from src.handler.student.student import HandlerViewProfile

filename_profile = "../../dbtest/StudentsProfile.json"
filename_classes = "../../dbtest/Classes.json"
filename_classes_done = "../../dbtest/StudentsClassesDone.json"

def new_wire_view_profile(request: StudentRequest):
    RepositoryViewProfile =

    mapper_handler = StudentMapper()
    use_case = StudentUseCase(RepositoryViewProfile)

    handler = HandlerViewProfile(mapper_handler, use_case)
    return handler.handler_view_profile(request)



def new_wire_view_class(request: ClassesRequest):
    repositoryViewClass =
    repositoryUpdateClassesDone =

    mapper_handler = ClassesMapper()
    use_case = ClassesUseCase(repositoryViewClass, repositoryUpdateClassesDone)

    handler = HandlerViewClass(mapper_handler, use_case)

    return handler.handler_view_class(request)
