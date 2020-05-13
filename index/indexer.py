import multiprocessing
from pathlib import Path


class Indexer:
    def __init__(self):
        self.index_dict = {}

    def _parse_file(self, path: Path) -> list:
        pass

    def create_index(self, list_of_paths: list, num_of_threads: int = 1) -> dict:
        pass

    def _merge(self):
        pass

    def _create_index_dict(self):
        pass
