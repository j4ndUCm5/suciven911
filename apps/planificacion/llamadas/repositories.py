from helpers.RepositoryMixin import Repository

from .models import Llamada


class LlamadaRepository(Repository):
    def __init__(self):
        self.entity = Llamada
