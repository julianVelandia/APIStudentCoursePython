from internal.classes.application.command.update import CommandUpdate
from internal.classes.domain.classes import Classes


class RepositoryViewClasses:
    def get_class_by_class_id(self, class_id: str) -> Classes:
        pass


class RepositoryUpdateClassesDone:
    def update_classes_by_email(self, cmd: CommandUpdate):
        pass


class ClassesUseCase(RepositoryViewClasses, RepositoryUpdateClassesDone):
    def __init__(self, repository_view_class, repository_update_classes_done):
        self.repository_view_class = repository_view_class
        self.repository_update_classes_done = repository_update_classes_done

    def execute(self, qry) -> Classes:
        domain_class = self.repository_view_class.get_class_by_class_id(qry.class_id())

        cmd = CommandUpdate(
            qry.email(),
            qry.class_id(),
            qry.title()
        )

        self.repository_update_classes_done.update_classes_by_email(cmd)

        return domain_class
