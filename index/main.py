from pathlib import Path
import time

from utils import generate_path_pattern, generate_list_of_paths


def main():
    directory = 'C:/Users/Smet/Desktop/3Course/Term2/Parallel/aclImdb/aclImdb'
    path = Path(directory)

    pattern = generate_path_pattern()
    paths = generate_list_of_paths(path, pattern)

    print(paths)
    print(len(paths))


if __name__ == '__main__':
    main()
