import os


def read_file(path: str):
    with open(path) as file:
        not_empty = [line for line in file.read().splitlines() if line]
    return list(set(not_empty))


def remove_file_if_exists(path: str):
    if os.path.exists(path):
        os.remove(path)
