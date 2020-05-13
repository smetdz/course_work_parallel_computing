from pathlib import Path
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
    files = [file for file in path.rglob('*.txt') if re.match(pattern, str(file)[len_path:])]

    return files
