from datetime import datetime

from internal.classes.domain.classes import Classes


class Mapper:
    def DTOClassToDomain(self, class_obj):
        return Classes(
            class_obj.ClassID,
            class_obj.Title,
            datetime.strptime(class_obj.CreationDate, "%Y-%m-%d"),
            class_obj.Content,
            class_obj.ReadTime,
        )
