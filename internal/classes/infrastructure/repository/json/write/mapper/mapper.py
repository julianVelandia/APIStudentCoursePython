from internal.classes.application.command.update import CommandUpdate
from internal.classes.infrastructure.repository.json.dto.classes import ClassesStudentDTO


class DTOClassesMapperWrite:
    def command_to_dto_class(self, cmd: CommandUpdate) -> ClassesStudentDTO:
        return ClassesStudentDTO(
            cmd.class_id(),
            cmd.title(),
        )
