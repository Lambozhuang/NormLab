from abc import ABC, abstractmethod
from pathlib import Path


class TraverseTool():
    def traverse_path(self, parent: Path):
        for child in parent.iterdir():
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
                    # print('FILE ' + str(child), sep='\n')
                    if child.suffix == '.zip':
                        self.handle_zip(child)
                    elif child.suffix == '.rar':
                        self.handle_rar(child)
                    else:
                        self.handle_other(child)
                else:
                    pass
                    # print('others')

    def check_ignore(self, path: Path) -> bool:
        return True

    def check_dir(self, path: Path):
        self.traverse_path(path)

    def handle_zip(self, file: Path):
        pass
        # print('ZIP ', file.name)
    
    def handle_rar(self, file: Path):
        pass
        # print('RAR ', file.name)

    def handle_other(self, file: Path):
        pass
        # print('OTHER ', file.name)