from typing import List

from internal.student.domain.profile import Profile, Classes


class ProfileRepositoryRead:
    def get_profile_by_email(self, email: str) -> Profile:
        pass


class ClassesDoneRepositoryRead:
    def get_classes_done_by_email(self, email: str) -> List[Classes]:
        pass


class StudentUseCase(ProfileRepositoryRead, ClassesDoneRepositoryRead):
    def __init__(
            self,
            repository_view_profile: ProfileRepositoryRead,
            repository_view_classes_done: ClassesDoneRepositoryRead,
    ):
        self.repository_view_profile = repository_view_profile
        self.repository_view_classes_done = repository_view_classes_done

    def execute(self, email: str) -> Profile:
        domain_profile = self.repository_view_profile.get_profile_by_email(email)
        domain_classes_done = self.repository_view_classes_done.get_classes_done_by_email(email)

        domain_profile.set_classes_done(domain_classes_done)

        return domain_profile
