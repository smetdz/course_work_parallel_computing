import multiprocessing as mlp
from pathlib import Path
from math import ceil


class Indexer:
    def __init__(self):
        self.index_dict = {}
        self.match_dict = {
            'test': '1',
            'train': '2',
            'neg': '3',
            'pos': '4',
            'unsup': '5',
        }

        self.reversed_match_dict = {item: key for key, item in self.match_dict.items()}

    @staticmethod
    def _string_conversion(message: str) -> list:
        symbols = ['.', ',', ';', '(', ')', '[', ']', ':', '?', '!', '<', '>', '\\', '/', '*', '"', '\'']

        for symbol in symbols:
            message = message.replace(symbol, '')

        return message.split()

    def _parse_file(self, path: Path) -> set:
        text = path.read_text('utf-8').lower()
        text = self._string_conversion(text)

        return set(text)

    def _generate_file_id(self, file_path: Path, dir_path_len: int) -> int:
        match_dict = self.match_dict

        d1, d2, file_name = str(file_path)[dir_path_len + 1:].split('\\')
        file_id = match_dict[d1] + match_dict[d2] + file_name.split('_')[0] + file_name.split('_')[1][0]

        return int(file_id)

    def create_index(self, dir_path: Path, list_of_paths: list, num_of_threads: int = 1) -> dict:
        dir_path_len = len(str(dir_path))

        if num_of_threads - 1:
            dicts_queue = mlp.Queue()

            offset = int(ceil(len(list_of_paths) / num_of_threads))
            threads = []

            for i in range(num_of_threads):
                threads.append(mlp.Process(target=self._mlp_create_index_dict,
                                           args=(list_of_paths[offset * i: offset * (i + 1)],
                                                 dir_path_len, dicts_queue)))

            for thread in threads:
                thread.start()

            for thread in threads:
                thread.join(timeout=0.01)

            self.index_dict = self._merge(dicts_queue, num_of_threads)
        else:
            self.index_dict = self._create_index_dict(list_of_paths, dir_path_len, {})

        return self.index_dict

    def _mlp_create_index_dict(self, list_of_path: list, dir_path_len: int, c_queue: mlp.Queue) -> None:
        dct = self._create_index_dict(list_of_path, dir_path_len, {})
        c_queue.put(dct)

    @staticmethod
    def _merge(dicts_queue: mlp.Queue, num_of_threads: int) -> dict:
        main_dict = dicts_queue.get()

        for _ in range(num_of_threads - 1):
            dct = dicts_queue.get()
            for lexeme, files_ids in dct.items():
                try:
                    main_dict[lexeme].update(files_ids)
                except KeyError:
                    main_dict[lexeme] = files_ids

        return main_dict

    def _create_index_dict(self, list_of_paths: list, dir_path_len: int, c_dict: dict) -> dict:
        for path in list_of_paths:
            file_id = self._generate_file_id(path, dir_path_len)
            lexemes = self._parse_file(path)

            for lexeme in lexemes:
                try:
                    c_dict[lexeme].add(file_id)
                except KeyError:
                    c_dict[lexeme] = {file_id, }

        return c_dict

    def _from_id_to_filename(self, path_id: int) -> str:
        mh_dct = self.reversed_match_dict

        str_id = str(path_id)
        return '\\'.join([mh_dct[str_id[0]], mh_dct[str_id[1]], str_id[2:-1] + '_' + str_id[-1] + '.txt'])

    def find_files(self, message: str) -> list:
        c_msg = self._string_conversion(message.lower())

        paths_ids = set()

        for word in c_msg:
            try:
                if not len(paths_ids):
                    paths_ids = self.index_dict[word]
                else:
                    paths_ids &= self.index_dict[word]
            except KeyError:
                continue

        paths = list(map(self._from_id_to_filename, paths_ids))

        return paths
