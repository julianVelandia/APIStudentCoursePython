import json

from internal.classes.domain.classes import Classes
from internal.classes.infrastructure.repository.json.dto.classes import ClassesDTO


class DTOClassesMapperRead:
    def dto_class_to_domain(self, class_obj: ClassesDTO) -> Classes:
        pass


class ClassesRepositoryRead(DTOClassesMapperRead):
    def __init__(self, mapper: DTOClassesMapperRead, filename_classes: str):
        self.mapper = mapper
        self.filename_classes = filename_classes

    def get_class_by_class_id(self, class_id: str) -> Classes:
        try:
            with open(self.filename_classes, 'r') as file:
                class_data = json.load(file)

            if class_id not in class_data:
                raise Exception(f"No class found for class_id: {class_id}")

            class_dto = ClassesDTO(**class_data[class_id])
            class_domain = self.mapper.dto_class_to_domain(class_dto)

            return class_domain
        except Exception as e:
            raise e
