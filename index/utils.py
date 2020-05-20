from pathlib import Path
from matplotlib import pyplot
import re


def generate_path_pattern() -> str:
    pattern_dir = [r'\\\w+\\\w{3}\\', r'\\\w+\\\w{5}\\', r'_\d+.txt', ]
    pattern_range1 = [r'1[56]\d{2}', r'17[0-4]\d', ]
    pattern_range2 = [r'6\d{3}', ]

    pattern = r'^'
    for ptr in pattern_range1:
        pattern += pattern_dir[0] + ptr + pattern_dir[2] + '|'

    for ptr in pattern_range2:
        pattern += pattern_dir[1] + ptr + pattern_dir[2] + '|'

    pattern = pattern[:-1] + '$'

    return pattern


def generate_list_of_paths(path: Path, pattern: str) -> list:
    len_path = len(str(path))
    paths = [file for file in path.rglob('*.txt') if re.match(pattern, str(file)[len_path:])]

    return paths


def draw_results(results: list, num_of_files: int):
    array_x = [elem[0] for elem in results]
    array_y = [elem[1] for elem in results]

    figure = pyplot.figure()
    ax = figure.add_subplot()
    # ax.set_xticks([num for num in range(len(array_x))])
    # ax.set_yticks(array_y)
    ax.set_xlabel('num of threads')
    ax.set_ylabel('time')
    ax.set_title(str(num_of_files), fontsize=15)
    ax.grid(True)
    ax.plot(array_x, array_y)
    pyplot.show()


def sameness_dict_check(dicts: list):
    if len(set(list(map(len, dicts)))) != 1:
        return False

    for key, value in dicts[0].items():
        for dct in dicts[1:]:
            if dct[key] != value:
                return False

    return True


