from internal.classes.application.usecase.view import ClassesUseCase
from internal.classes.infrastructure.repository.json.read.classes import ClassesRepositoryRead, DTOClassesMapperRead
from internal.classes.infrastructure.repository.json.write.classes_student import ClassesRepositoryWrite, \
    DTOClassesMapperWrite
from internal.student.application.usecase.view_profile import StudentUseCase
from internal.student.infrastructure.repository.json.read.classes_done import ClassesDoneRepositoryRead
from internal.student.infrastructure.repository.json.read.profile import ProfileRepositoryRead
from internal.student.infrastructure.repository.json.read.mapper.mapper import DTOStudentMapper
from src.handler.classes.classes import HandlerViewClass, ClassesMapper
from src.handler.classes.contract.request import ClassesRequest
from src.handler.student.contract.request import StudentRequest
from src.handler.student.mapper.mapper import StudentMapper
from src.handler.student.student import HandlerViewProfile

filename_profile = "dbtest/StudentsProfile.json"
filename_classes = "dbtest/Classes.json"
filename_classes_done = "dbtest/StudentsClassesDone.json"


def new_wire_view_profile(request: StudentRequest):
    repository_view_profile = ProfileRepositoryRead(
        DTOStudentMapper(),
        filename_profile,
    )
    repository_view_classes_done = ClassesDoneRepositoryRead(
        DTOStudentMapper(),
        filename_classes_done,
    )

    mapper_handler = StudentMapper()
    use_case = StudentUseCase(
        repository_view_profile,
        repository_view_classes_done,
    )

    handler = HandlerViewProfile(mapper_handler, use_case)
    return handler.handler_view_profile(request)


def new_wire_view_class(request: ClassesRequest):
    repository_view_classes = ClassesRepositoryRead(
        DTOClassesMapperRead(),
        filename_classes,
    )
    repository_update_classes_done = ClassesRepositoryWrite(
        DTOClassesMapperWrite(),
        filename_classes_done,
    )

    mapper_handler = ClassesMapper()
    use_case = ClassesUseCase(repository_view_classes, repository_update_classes_done)

    handler = HandlerViewClass(mapper_handler, use_case)

    return handler.handler_view_class(request)
