from pathlib import Path
import time

from utils import generate_file_pattern, generate_list_of_files


def main():
    directory = 'C:/Users/Smet/Desktop/3Course/Term2/Parallel/aclImdb/aclImdb'
    path = Path(directory)

    pattern = generate_file_pattern()
    files = generate_list_of_files(path, pattern)

    print(files)
    print(len(files))


if __name__ == '__main__':
    main()
