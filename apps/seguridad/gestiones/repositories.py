from helpers.RepositoryMixin import Repository

from .models import Gestion


class GestionRepository(Repository):
    def __init__(self):
        self.entity = Gestion
