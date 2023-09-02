from internal.classes.application.command.update import CommandUpdate
from internal.classes.infrastructure.repository.json.dto.classes import ClassesStudentDTO


class Mapper:
    def CommandToDTOClass(self, cmd: CommandUpdate) -> ClassesStudentDTO:
        return ClassesStudentDTO(
            cmd.class_id(),
            cmd.title(),
        )
