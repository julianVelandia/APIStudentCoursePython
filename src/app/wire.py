from src.handler.classes.classes import HandlerViewClass
from src.handler.classes.contract import ClassRequest
from src.handler.classes.mapper.mapper import ClassMapper
from src.handler.student.contract import StudentRequest
from src.handler.student.mapper.mapper import StudentMapper
from src.handler.student.student import HandlerViewProfile

filename_profile = "../../dbtest/StudentsProfile.json"
filename_classes = "../../dbtest/Classes.json"
filename_classes_done = "../../dbtest/StudentsClassesDone.json"




def new_wire_view_profile(request: StudentRequest):
    mapper_handler = StudentMapper()
    use_case =

    handler = HandlerViewProfile(mapper_handler, use_case)
    return handler.handler_view_profile(request)



def new_wire_view_class(request: ClassRequest):
    mapper_handler = ClassMapper()
    use_case =

    handler = HandlerViewClass(mapper_handler, use_case)

    return handler.handler_view_class(request)
