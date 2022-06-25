from pathlib import Path
from archive_tool import UnarchiveTool
from traverse_tool import TraverseTool


class LabController():
    # self.__full_name: str
    # self.__id: str
    # self.__path: Path
    # self.__short_name: str

    def __init__(self, path: Path) -> None:
        self.__zip_path = path
        self.__path = path.parent / path.stem

    def execute(self, tool: TraverseTool) -> None:
        if tool.__class__ == UnarchiveTool:
            tool.traverse_path(self.__zip_path)
        else:
            tool.traverse_path(self.__path)

    def export(self, path: Path) -> None:
        pass


if __name__ == '__main__':
    pass