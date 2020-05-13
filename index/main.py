from pathlib import Path
import time

from utils import generate_path_pattern, generate_list_of_paths
from indexer import Indexer


def main():
    dir_path = 'C:/Users/Smet/Desktop/3Course/Term2/Parallel/aclImdb/aclImdb'
    path = Path(dir_path)

    pattern = generate_path_pattern()
    paths = generate_list_of_paths(path, pattern)

    # print(paths)
    # print(len(paths))

    start = time.time()

    indexer = Indexer()

    # paths = [p for p in path.rglob('*.txt')]

    d = indexer.create_index(path, paths)

    end = time.time() - start

    print(len(d))

    print(f'{end}')
    print(f'{indexer.count}')

    c = 0
    for k, i in d.items():
        c += len(i)

    print(c)


if __name__ == '__main__':
    main()
