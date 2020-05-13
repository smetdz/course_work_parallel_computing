from pathlib import Path
import time

from utils import generate_path_pattern, generate_list_of_paths
from indexer import Indexer


def main():
    dir_path = 'C:/Users/Smet/Desktop/3Course/Term2/Parallel/aclImdb/aclImdb'
    path = Path(dir_path)

    pattern = generate_path_pattern()
    paths = generate_list_of_paths(path, pattern)

    start = time.time()

    indexer = Indexer()
    d = indexer.create_index(path, paths)

    end = time.time() - start
    print(f'{end}')

    print(len(d))


if __name__ == '__main__':
    main()
