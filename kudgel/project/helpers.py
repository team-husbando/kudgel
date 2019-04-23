from kudgel.user.models import User
from kudgel.project.models import Project


class ProjectHelpers():
    model = Project

    def CreateStaffForProject(self, user_name, project):
        self.model.team.create()
