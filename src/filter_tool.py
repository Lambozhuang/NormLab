from pathlib import Path
from traverse_tool import TraverseTool
from common_tool import ignore_list
from shutil import rmtree

class FilterTraverseTool(TraverseTool):
    def __init__(self) -> None:
        super().__init__()

    def check_ignore(self, path: Path) -> bool:
        print(path.stem)
        if path.stem in ignore_list:
            if path.is_dir():
                rmtree(path)
            elif path.is_file():
                path.unlink()
            return False
        else:
            return True
