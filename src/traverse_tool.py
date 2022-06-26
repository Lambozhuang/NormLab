from abc import ABC, abstractmethod
from pathlib import Path
from tkinter import W
from common_tool import ignore_list

class TraverseTool():
    def traverse_path(self, parent: Path):
        if parent.is_file():
            self.handle_file(parent)
        elif parent.is_dir():
            empty = True
            for child in parent.iterdir():
                empty = False
                if self.check_ignore(child):
                    if child.is_dir():

                        # Check empty
                        flag = False
                        for _ in child.iterdir():
                            flag = True
                            break

                        if flag: # not empty
                            self.check_dir(child)
                        else:
                            child.rmdir()
                    elif child.is_file():
                        self.handle_file(child)
                    else:
                        pass
            if empty:
                parent.rmdir()

    def check_ignore(self, path: Path) -> bool:
        if path.name in ignore_list:
            return False
        return True

    def check_dir(self, path: Path):
        self.traverse_path(path)

    def handle_file(self, path: Path) -> None:
        pass
