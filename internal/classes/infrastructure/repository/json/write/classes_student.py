import json

from internal.classes.application.command.update import CommandUpdate
from internal.classes.infrastructure.repository.json.dto.classes import ClassesStudentDTO


class Mapper:
    def CommandToDTOClass(self, cmd: CommandUpdate) -> ClassesStudentDTO:
        return ClassesStudentDTO(
            cmd.class_id(),
            cmd.title(),
        )


class ClassRepositoryWrite(Mapper):
    def __init__(self, mapper: Mapper, filename_classes_done: str):
        self.mapper = mapper
        self.filename_classes_done = filename_classes_done

    def UpdateClassesByEmail(self, cmd: CommandUpdate) -> None:
        try:
            with open(self.filename_classes_done, 'r') as file:
                classes_done_by_user = json.load(file)
        except FileNotFoundError:
            classes_done_by_user = {}

        email = cmd.email()

        new_class = self.mapper.CommandToDTOClass(cmd)

        if email not in classes_done_by_user:
            classes_done_by_user[email] = []
        classes_done_by_user[email].append(new_class)

        with open(self.filename_classes_done, 'w') as file:
            json.dump(classes_done_by_user, file, indent=2)
