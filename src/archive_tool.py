from zipfile import *
from rarfile import *
from pathlib import Path
from filter_tool import check_chaoxing_file
from traverse_tool import TraverseTool
from common_tool import *


class ArchiveFile:
    def __init__(self) -> None:
        pass

    def extract_all(self, path: Path)  :
        self.extractall(path)

    def extract_one(self, info, out_path: Path):
        if info.filename not in ignore_list:
            try:
                info.filename = info.filename.encode('cp437').decode('gbk')
            except UnicodeDecodeError:
                info.filename = info.filename.encode('cp437').decode('utf-8')
            if check_chaoxing_file(info.filename):
                self.extract(info, out_path)
    
class CustomZipFile(ArchiveFile, ZipFile):
    def __init__(self, file: Path) -> None:
        ArchiveFile.__init__(self)
        ZipFile.__init__(self, file, 'r')

class CustomRarFile(ArchiveFile, RarFile):
    def __init__(self, file: Path) -> None:
        ArchiveFile.__init__(self)
        RarFile.__init__(self, file)

class UnarchiveTool(TraverseTool):
    def __init__(self) -> None:
        super().__init__()
        self.ArchiveClass = ArchiveFile

    def handle_file(self, path: Path, output_path: Path = None) -> None:
        if self.check_file_type(path.suffix):
            if output_path == None:
                out_path = path.parent / path.stem
            else:
                out_path = output_path
            archive_file = self.ArchiveClass(path)
            for info in archive_file.infolist():
                archive_file.extract_one(info, out_path)
            archive_file.close()
            path.unlink()
            self.traverse_path(out_path)
        else:
            pass

    def check_file_type(self, suffix: str):
        if suffix == '.zip':
            self.ArchiveClass = CustomZipFile
            return True
        elif suffix == '.rar':
            return False
            self.ArchiveClass = CustomRarFile
            return True
        else:
            return False
