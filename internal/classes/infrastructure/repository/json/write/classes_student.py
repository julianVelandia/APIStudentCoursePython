import json

from internal.classes.application.command.update import CommandUpdate
from internal.classes.infrastructure.repository.json.dto.classes import ClassesStudentDTO


class DTOClassesMapperWrite:
    def command_to_dto_class(self, cmd: CommandUpdate) -> ClassesStudentDTO:
        return ClassesStudentDTO(
            cmd.class_id(),
            cmd.title(),
        )


class ClassesRepositoryWrite(DTOClassesMapperWrite):
    def __init__(self, mapper: DTOClassesMapperWrite, filename_classes_done: str):
        self.mapper = mapper
        self.filename_classes_done = filename_classes_done

    def update_classes_by_email(self, cmd: CommandUpdate) -> None:
        try:
            with open(self.filename_classes_done, 'r') as file:
                classes_done_by_user = json.load(file)
        except FileNotFoundError:
            classes_done_by_user = {}

        email = cmd.email()

        new_class = self.mapper.command_to_dto_class(cmd)

        if email not in classes_done_by_user:
            classes_done_by_user[email] = []
        classes_done_by_user[email].append(new_class)

        with open(self.filename_classes_done, 'w') as file:
            json.dump(classes_done_by_user, file, indent=2)
