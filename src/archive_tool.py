from zipfile import *
from rarfile import *
from filter_tool import check_chaoxing_file
from traverse_tool import TraverseTool
from pathlib import Path

class ArchiveFile:
    def __init__(self) -> None:
        pass

    def extract_all(self, path: Path)  :
        self.extractall(path)

    def extract_one(self, zip_info: ZipInfo, path: Path):
        # TODO: infolist 自己就有，不用传进来
        try:
            zip_info.filename = zip_info.filename.encode('cp437').decode('gbk')
        except UnicodeDecodeError:
            zip_info.filename = zip_info.filename.encode('cp437').decode('utf-8')
        except UnicodeDecodeError:
            pass
        if check_chaoxing_file(zip_info.filename):
            self.extract(zip_info, path)
    
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

    # def handle_zip(self, file: Path, path: Path = None):
    #     if path == None:
    #         path = file.parent / file.stem

    #     zipfile = CustomZipFile(file)
    #     for zip_info in zipfile.infolist():
    #         zipfile.extract_one(zip_info, path)
    #     zipfile.close()
    #     # file.unlink()
    #     print(path)
    #     self.traverse_path(path)

    def handle_file(self, path: Path) -> None:
        if self.check_file_type(path.suffix):
            out_path = path.parent / path.stem
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
            self.ArchiveClass = CustomRarFile
            return True
        else:
            return False
