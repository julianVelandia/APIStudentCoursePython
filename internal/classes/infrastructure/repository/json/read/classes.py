import json

from internal.classes.domain.classes import Classes
from internal.classes.infrastructure.repository.json.dto.classes import ClassesDTO


class Mapper:
    def DTOClassToDomain(self, class_obj: ClassesDTO) -> Classes:
        pass


class ClassRepositoryRead(Mapper):
    def __init__(self, mapper: Mapper, filename_classes: str):
        self.mapper = mapper
        self.filename_classes = filename_classes

    def GetClassByClassID(self, class_id: str) -> Classes:
        try:
            with open(self.filename_classes, 'r') as file:
                class_data = json.load(file)

            if class_id not in class_data:
                raise Exception(f"No class found for class_id: {class_id}")

            class_dto = ClassesDTO(**class_data[class_id])
            class_domain = self.mapper.DTOClassToDomain(class_dto)

            return class_domain
        except Exception as e:
            raise e
