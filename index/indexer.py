import multiprocessing
from pathlib import Path


class Indexer:
    def __init__(self):
        self.index_dict = {}
        self.count = 0

    @staticmethod
    def _parse_file(path: Path) -> list:
        symbols = ['.', ',', ';', '(', ')', '[', ']', ':', '?', '<' '>' '\\', '/']
        text = path.read_text('utf-8')

        for symbol in symbols:
            text = text.replace(symbol, '')

        return text.split()

    @staticmethod
    def _generate_file_id(file_path: Path, dir_path_len: int) -> int:
        match_dict = {
            'test': '1',
            'train': '2',
            'neg': '1',
            'pos': '2',
            'unsup': '3',
        }

        d1, d2, file_name = str(file_path)[dir_path_len + 1:].split('\\')
        file_id = match_dict[d1] + match_dict[d2] + file_name.split('_')[0]

        return int(file_id)

    def create_index(self, dir_path: Path, list_of_paths: list, num_of_threads: int = 1) -> dict:
        dir_path_len = len(str(dir_path))
        d = self._create_index_dict(list_of_paths, dir_path_len, {})
        return d

    def _merge(self):
        pass

    def _create_index_dict(self, list_of_paths: list, dir_path_len: int, c_dict: dict):
        for path in list_of_paths:
            file_id = self._generate_file_id(path, dir_path_len)
            lexemes = self._parse_file(path)

            for lexeme in lexemes:
                self.count += 1
                try:
                    c_dict[lexeme].add(file_id)
                except KeyError:
                    c_dict[lexeme] = {file_id, }

        return c_dict
