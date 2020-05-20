from pathlib import Path
import time

from utils import generate_path_pattern, generate_list_of_paths, draw_results, sameness_dict_check
from indexer import Indexer


def main():
    dir_path = 'C:/Users/Smet/Desktop/3Course/Term2/Parallel/aclImdb/aclImdb'
    path = Path(dir_path)

    pattern = generate_path_pattern()
    paths = generate_list_of_paths(path, pattern)

    num_of_files = len(paths)

    indexer = Indexer()

    results = []
    index_dicts = []
    while True:
        num_of_threads = input('Enter num of threads or "quit" if you want to see the results: ')

        if num_of_threads == 'quit':
            break

        num_of_threads = int(num_of_threads)

        start = time.time()
        index_dicts.append(indexer.create_index(path, paths, num_of_threads))
        end = time.time() - start

        results.append((num_of_threads, end))

        print(f'{end}')

    draw_results(results, num_of_files)
    print(sameness_dict_check(index_dicts))


if __name__ == '__main__':
    main()
