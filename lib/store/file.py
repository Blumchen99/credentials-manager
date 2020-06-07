from typing import List


# TODO: lock files
def write_lines(
        filename: str,
        path: str,
        lines: List[str]
):
    f = open(path + filename, "w+")
    for line in lines:
        f.write(line + "\n")
    f.close()
