from pathlib import Path
from traverse_tool import TraverseTool
from common_tool import ignore_list
from shutil import rmtree
from os import listdir

class FilterTraverseTool(TraverseTool):
    def __init__(self) -> None:
        super().__init__()

    def check_ignore(self, path: Path) -> bool:
        # print(path.stem)
        if path.stem in ignore_list:
            if path.is_dir():
                rmtree(path)
            elif path.is_file():
                path.unlink()
            return False
        else:
            return True

    def check_dir(self, path: Path):
        print(str(path), end='\n')
        print(len(listdir(str(path.parent))))
        if path.parent.name == path.name and len(listdir(str(path.parent))) == 1: # TODO: implement FUZZ
            path = path.replace(path.parent / 'temp')
            for child in path.iterdir():
                child.rename(child.parent.parent / child.name)
            parent = path.parent
            rmtree(path)
            self.traverse_path(parent)
        else:
            self.traverse_path(path)