from pathlib import Path
from thefuzz import fuzz
from pip import List
from src.traverse_tool import TraverseTool
from src.common_tool import *
from shutil import rmtree
from os import listdir

class FileFilterTool(TraverseTool):
    def __init__(self) -> None:
        super().__init__()

    def check_ignore(self, path: Path) -> bool:
        # print(path.stem)
        if path.stem in ignore_list:
            # print(path.name)
            if path.is_dir():
                rmtree(path)
            elif path.is_file():
                path.unlink()
            return False
        else:
            return True

class FindDocTool(TraverseTool):
    def __init__(self) -> None:
        super().__init__()
        self.__doc_path_list: List[Path] = []

    def handle_file(self, path: Path) -> None:
        if path.suffix in doc_list:
            self.__doc_path_list.append(path)

    def get_doc_path_list(self):
        return self.__doc_path_list

    def reset(self):
        self.__doc_path_list: List[Path] = []

class StructureFilterTool(TraverseTool):
    def __init__(self) -> None:
        super().__init__()

    def check_dir(self, path: Path):
        if fuzz.ratio(path.parent.name, path.name) > 50 and len(listdir(str(path.parent))) == 1:
            path = path.replace(path.parent / 'temp')
            for child in path.iterdir():
                pass
                try:
                    child.rename(child.parent.parent / child.name)
                except FileExistsError:
                    new_name = child.name + '-2'
                    child.rename(child.parent / new_name)
            parent = path.parent
            rmtree(path)
            self.traverse_path(parent)
        else:
            self.traverse_path(path)


def check_chaoxing_file(name: str) -> bool:
    if name[:len(ignore_chaoxing)] == ignore_chaoxing and name[-4:] == '.doc':
        return False
    else:
        return True