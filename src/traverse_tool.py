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

                    if flag:
                        print('DIR ' + str(child), sep='\t')
                        self.traverse_path(child)
                    else:
                        print('EMPTY DIR ' + str(child), sep='\t')
                elif child.is_file():
                    print('FILE ' + str(child), sep='\n')
                    if child.suffix == '.zip':
                        self.handle_zip(child)
                    elif child.suffix == '.rar':
                        self.handle_rar(child)
                    else:
                        self.handle_other(child)
                else:
                    print('others')

    def check_ignore(self, path: Path) -> bool:
        return True

    def handle_zip(self, file: Path):
        pass
        # print('ZIP ', file.name)
    
    def handle_rar(self, file: Path):
        pass
        # print('RAR ', file.name)

    def handle_other(self, file: Path):
        pass
        # print('OTHER ', file.name)