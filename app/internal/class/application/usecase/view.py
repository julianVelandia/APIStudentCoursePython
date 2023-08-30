from abc import ABC, abstractmethod

class RepositoryViewClass(ABC):
    @abstractmethod
    def get_class_by_class_id(self, class_id):
        pass

class RepositoryUpdateClassesDone(ABC):
    @abstractmethod
    def update_classes_by_email(self, cmd):
        pass

class ViewUseCase:
    def __init__(self, repository_view_class, repository_update_classes_done):
        self.repository_view_class = repository_view_class
        self.repository_update_classes_done = repository_update_classes_done

    def execute(self, qry):
        domain_class, err = self.repository_view_class.get_class_by_class_id(qry.class_id())
        if err is not None:
            return domain_class, err

        cmd = command.new_update(
            qry.email(),
            qry.class_id(),
            qry.title()
        )
        err = self.repository_update_classes_done.update_classes_by_email(cmd)
        if err is not None:
            return domain_class, err

        return domain_class, None
